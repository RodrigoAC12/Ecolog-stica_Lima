#!/usr/bin/env python3
"""Validate repository-local links in Markdown files without network access."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^)]+))\s*\)")
SKIP_DIRS = {".git", ".venv", "node_modules", "vendor", "dist", "build"}


def check_links() -> list[str]:
    broken: list[str] = []
    md_files = sorted(
        p for p in ROOT.rglob("*.md") if not set(p.relative_to(ROOT).parts) & SKIP_DIRS
    )
    for source in md_files:
        fenced = False
        for lineno, line in enumerate(source.read_text(encoding="utf-8").splitlines(), start=1):
            if line.lstrip().startswith((chr(96) * 3, "~~~")):
                fenced = not fenced
                continue
            if fenced:
                continue
            for match in LINK.finditer(line):
                raw = (match.group(1) or match.group(2)).strip()
                raw = re.sub(r'\s+["\x27][^"\x27]*["\x27]$', "", raw)
                if not raw or raw.startswith(("#", "/", "mailto:", "data:")):
                    continue
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", raw):
                    continue
                path = unquote(raw.split("#", 1)[0].split("?", 1)[0])
                if not path:
                    continue
                target = (source.parent / path).resolve()
                if not target.is_relative_to(ROOT) or not target.exists():
                    relative = source.relative_to(ROOT)
                    broken.append(f"{relative}:{lineno}: {raw} -> missing {path}")
    return broken


if __name__ == "__main__":
    missing = check_links()
    if missing:
        print(f"Found {len(missing)} broken local Markdown links:")
        for problem in missing:
            print(" -", problem)
        sys.exit(1)
    print("Local Markdown file links are valid.")
