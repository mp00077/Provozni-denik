"""Ruční nativní build; tento skript se nespouští automaticky."""
import subprocess
import sys
import shutil
from generate_ui import ROOT, generate
from build_metadata import git_version


def clean_outputs(root=ROOT):
    root = root.resolve(strict=True)
    targets = [root / "build", root / "dist" / "provozní deník"]
    # Ověřit i rodičovský dist; maže se jen konkrétní výstup aplikace.
    for target in [root / "build", root / "dist", targets[1]]:
        if target.is_symlink() or (hasattr(target, "is_junction") and target.is_junction()):
            raise RuntimeError(f"Výstupní adresář nesmí být odkaz: {target}")
        if target.resolve() != target or not target.resolve().is_relative_to(root):
            raise RuntimeError(f"Výstupní adresář leží mimo projekt: {target}")
        if target.exists() and not target.is_dir():
            raise RuntimeError(f"Výstupní cesta není adresář: {target}")
    for target in targets:
        if target.exists():
            print(f"Odstraňuji {target}")
            shutil.rmtree(target)


def main():
    version = git_version(ROOT)
    print(f"Build pro {sys.platform}, Git tag: {version.tag}" if version else
          f"Build pro {sys.platform}: Git tag není dostupný, verzi vynechávám.")
    clean_outputs()
    generate()
    subprocess.run([sys.executable, "-m", "PyInstaller", "--noconfirm",
                    "--distpath", str(ROOT / "dist"),
                    "--workpath", str(ROOT / "build" / sys.platform),
                    str(ROOT / "packaging/app.spec")], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
