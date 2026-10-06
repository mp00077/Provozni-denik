import json
from pathlib import Path

_metadata = Path(__file__).resolve().parents[1] / "_build_metadata.json"
VERSION = (json.loads(_metadata.read_text(encoding="utf-8"))["version"] or "bez verze") if _metadata.is_file() else "0.1.0"
