"""Store local Windows settings encrypted for the current account with DPAPI."""
import ctypes
import json
import os
from ctypes import wintypes
from pathlib import Path


class _Blob(ctypes.Structure):
    _fields_ = [("size", wintypes.DWORD), ("data", ctypes.POINTER(ctypes.c_ubyte))]


def _crypt(payload: bytes, *, decrypt: bool = False) -> bytes:
    if os.name != "nt":
        raise OSError("La configuración protegida utiliza DPAPI de Windows")
    source_buffer = ctypes.create_string_buffer(payload)
    source = _Blob(len(payload), ctypes.cast(source_buffer, ctypes.POINTER(ctypes.c_ubyte)))
    result = _Blob()
    library = ctypes.WinDLL("crypt32", use_last_error=True)
    function = library.CryptUnprotectData if decrypt else library.CryptProtectData
    function.argtypes = [ctypes.POINTER(_Blob), ctypes.c_void_p, ctypes.c_void_p,
                         ctypes.c_void_p, ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(_Blob)]
    function.restype = wintypes.BOOL
    # CRYPTPROTECT_UI_FORBIDDEN: do not display credential or permission dialogs.
    if not function(ctypes.byref(source), None, None, None, None, 1, ctypes.byref(result)):
        raise ctypes.WinError(ctypes.get_last_error())
    free = ctypes.WinDLL("kernel32", use_last_error=True).LocalFree
    free.argtypes = [ctypes.c_void_p]
    free.restype = ctypes.c_void_p
    try:
        return ctypes.string_at(result.data, result.size)
    finally:
        free(result.data)


def settings_directory() -> Path:
    return Path(os.environ["LOCALAPPDATA"]) / "EcoLogistica"


def _decode(payload: bytes) -> dict[str, str]:
    values = json.loads(_crypt(payload, decrypt=True).decode("utf-8"))
    if not isinstance(values, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in values.items()):
        raise ValueError("Formato de configuración protegida inválido")
    return values


def save_settings(values: dict[str, str], directory: Path | None = None) -> Path:
    directory = directory or settings_directory()
    directory.mkdir(parents=True, exist_ok=True)
    destination = directory / "staging.settings.dpapi"
    encrypted = _crypt(json.dumps(values, ensure_ascii=False).encode("utf-8"))
    with destination.open("xb") as stream:
        stream.write(encrypted)
    if _decode(destination.read_bytes()) != values:
        raise OSError("No se pudo comprobar la configuración protegida")
    return destination


def load_settings(directory: Path | None = None) -> dict[str, str]:
    directory = directory or settings_directory()
    destination = directory / "staging.settings.dpapi"
    legacy = directory / "staging.env"
    if destination.exists():
        return _decode(destination.read_bytes())
    if not legacy.exists():
        raise FileNotFoundError("Ejecutar primero scripts/prepare_local_staging.py")
    values = dict(line.split("=", 1) for line in legacy.read_text(encoding="utf-8").splitlines()
                  if line and not line.startswith("#"))
    save_settings(values, directory)
    # Remove only the legacy file after an encrypted round trip verified every value.
    legacy.unlink()
    return values
