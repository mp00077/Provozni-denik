"""Ruční nativní build; tento skript se nespouští automaticky."""
import subprocess
import sys
from generate_ui import ROOT, generate


def main():
    generate()
    subprocess.run([sys.executable, "-m", "PyInstaller", "--noconfirm",
                    "--distpath", str(ROOT / "dist" / sys.platform),
                    "--workpath", str(ROOT / "build" / sys.platform),
                    str(ROOT / "packaging/app.spec")], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
