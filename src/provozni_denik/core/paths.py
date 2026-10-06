import sys
from pathlib import Path


def application_directory() -> Path:
    """Stabilní cesta aplikace; nezávisí na pracovním adresáři ani _MEIPASS."""
    if getattr(sys, "frozen", False):
        executable = Path(sys.executable).resolve()
        if sys.platform == "darwin":
            for parent in executable.parents:
                if parent.suffix == ".app":
                    return parent.parent
        return executable.parent
    return Path(__file__).resolve().parents[3]


def data_directory() -> Path:
    return application_directory() / "db"
