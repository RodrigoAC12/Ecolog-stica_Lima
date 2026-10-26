"""Integration checks of encryption and lossless migration on Windows."""
import contextlib
import io
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from local_staging_settings import load_settings, save_settings
from prepare_local_staging import prepare


@unittest.skipUnless(os.name == "nt", "DPAPI is a Windows facility")
class ProtectedSettingsTests(unittest.TestCase):
    def test_encrypted_round_trip_does_not_store_the_secret(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            values = {"POSTGRES_PASSWORD": "test-only-secret-not-for-use", "JWT_SECRET": "otra-clave-de-prueba"}
            destination = save_settings(values, directory)
            self.assertNotIn(values["POSTGRES_PASSWORD"].encode(), destination.read_bytes())
            self.assertEqual(load_settings(directory), values)

    def test_migration_preserves_values_and_removes_only_the_plaintext_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            legacy = directory / "staging.env"
            legacy.write_text("POSTGRES_PASSWORD=test-only-password\nJWT_SECRET=test=with=equals\n", encoding="utf-8")
            values = load_settings(directory)
            self.assertEqual(values, {"POSTGRES_PASSWORD": "test-only-password", "JWT_SECRET": "test=with=equals"})
            self.assertFalse(legacy.exists())
            protected = (directory / "staging.settings.dpapi").read_bytes()
            self.assertEqual(load_settings(directory), values)
            self.assertEqual((directory / "staging.settings.dpapi").read_bytes(), protected)

    def test_corrupt_ciphertext_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            destination = save_settings({"setting": "test-data"}, directory)
            payload = bytearray(destination.read_bytes())
            payload[-1] ^= 1
            destination.write_bytes(payload)
            with self.assertRaises(OSError):
                load_settings(directory)

    def test_prepare_preserves_existing_credentials_without_printing_them(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / "EcoLogistica"
            values = {"POSTGRES_PASSWORD": "test-only-existing-secret", "JWT_SECRET": "test-key"}
            destination = save_settings(values, directory)
            before = destination.read_bytes()
            output = io.StringIO()
            with patch.dict(os.environ, {"LOCALAPPDATA": temporary}), contextlib.redirect_stdout(output):
                prepare()
            self.assertEqual(load_settings(directory), values)
            self.assertEqual(destination.read_bytes(), before)
            self.assertNotIn(values["POSTGRES_PASSWORD"], output.getvalue())


if __name__ == "__main__":
    unittest.main()
