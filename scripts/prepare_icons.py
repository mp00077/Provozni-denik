"""Převod schválené PNG ikony do nativních formátů; není součástí buildu."""
import argparse
from pathlib import Path
from shutil import copyfile


def convert(source: Path, root: Path) -> None:
    from PIL import Image

    output = root / "packaging/icons"
    output.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as original:
        image = original.convert("RGBA")
        image = image.resize((1024, 1024), Image.Resampling.LANCZOS)
        image.save(output / "app.png")
        image.save(output / "app.ico", sizes=[(size, size) for size in (16, 24, 32, 48, 64, 128, 256)])
        image.save(output / "app.icns", sizes=[(size, size) for size in (16, 32, 64, 128, 256, 512, 1024)])
    runtime = root / "src/provozni_denik/ui/resources/icons"
    runtime.mkdir(parents=True, exist_ok=True)
    copyfile(output / "app.png", runtime / "app.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    arguments = parser.parse_args()
    convert(arguments.source, Path(__file__).resolve().parents[1])
