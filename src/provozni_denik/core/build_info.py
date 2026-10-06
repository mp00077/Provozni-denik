"""Údaje sestavení se čtou z přibalených metadat, nikoli z počítače uživatele."""
import json
import platform
import subprocess
import sys
from pathlib import Path


def _git(root: Path, *arguments: str) -> str | None:
    try:
        result = subprocess.run(["git", *arguments], cwd=root, capture_output=True,
                                text=True, encoding="utf-8", check=True, timeout=3,
                                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)
        return result.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def load_build_info() -> dict:
    package = Path(__file__).resolve().parents[1]
    metadata = package / "_build_metadata.json"
    if metadata.is_file():
        return json.loads(metadata.read_text(encoding="utf-8"))
    info = {"author": "Miroslav Pospíšil", "built_at": None,
            "git_tag": None, "git_commit": None, "python_version": platform.python_version()}
    # Zabalená aplikace nikdy nehledá Git v cizí pracovní složce.
    if not getattr(sys, "frozen", False):
        root = package.parents[1]
        if (root / ".git").exists():
            info["git_tag"] = _git(root, "describe", "--tags", "--abbrev=0", "HEAD")
            info["git_commit"] = _git(root, "rev-parse", "HEAD")
    return info
