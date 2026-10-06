import sqlite3
from pathlib import Path


def backup(connection, source, destination):
    destination = Path(destination)
    if destination.resolve() == Path(source).resolve():
        raise ValueError("Záloha musí mít jinou cestu než provozní databáze.")
    target = sqlite3.connect(destination)
    try:
        with target:
            connection.backup(target)
    finally:
        target.close()
