"""Run Compose with protected settings in memory, without a plaintext secrets file."""
import os
import subprocess
import sys
from pathlib import Path

from local_staging_settings import load_settings


def main() -> int:
    repository = Path(__file__).resolve().parents[1]
    arguments = sys.argv[1:] or ["ps"]
    if arguments[0] == "config" and "--quiet" not in arguments:
        raise SystemExit("Usar config --quiet para no mostrar los valores operativos")
    environment = {**os.environ, **load_settings()}
    command = ["docker", "compose", "--env-file", str(repository / ".env.staging.example"),
               "-p", "ecologistica-staging-local", "-f", str(repository / "docker-compose.staging.yml"),
               *arguments]
    return subprocess.run(command, cwd=repository, env=environment, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
