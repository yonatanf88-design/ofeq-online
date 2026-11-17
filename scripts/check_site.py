#!/usr/bin/env python3
"""Extract and validate the inline JS from the published HTML."""
from pathlib import Path
import re
import subprocess
import tempfile

html = (Path(__file__).resolve().parents[1] / "site" / "index.html").read_text(encoding="utf-8")
scripts = re.findall(r"<script(?:\s[^>]*)?>([\s\S]*?)</script>", html, flags=re.IGNORECASE)
if len(scripts) != 1:
    raise SystemExit(f"Expected one inline JS block, found {len(scripts)}")
with tempfile.TemporaryDirectory() as folder:
    script = Path(folder) / "ofeq-inline.js"
    script.write_text(scripts[0], encoding="utf-8")
    subprocess.run(["node", "--check", str(script)], check=True)
print("Ofeq inline JS parses successfully")
