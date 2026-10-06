"""Generuje Qt formuláře pomocí nástrojů ze stejného Python prostředí."""
from pathlib import Path
import subprocess
import sys
import sysconfig

ROOT = Path(__file__).resolve().parents[1]


def qt_tool(name):
    suffix = ".exe" if sys.platform == "win32" else ""
    tool = Path(sysconfig.get_path("scripts")) / (name + suffix)
    if not tool.is_file():
        raise RuntimeError(f"Chybí {tool}. Nainstalujte závislosti do tohoto Python prostředí.")
    return str(tool)


def generate():
    ui = ROOT / "src/provozni_denik/ui"
    output = ui / "generated"
    output.mkdir(parents=True, exist_ok=True)
    (output / "__init__.py").touch()
    for form in sorted((ui / "forms").glob("*.ui")):
        subprocess.run([qt_tool("pyside6-uic"), str(form), "-o", str(output / (form.stem + ".py"))], check=True)
    for resource in sorted((ui / "resources").glob("*.qrc")):
        subprocess.run([qt_tool("pyside6-rcc"), str(resource), "-o", str(output / (resource.stem + "_rc.py"))], check=True)


if __name__ == "__main__":
    generate()
