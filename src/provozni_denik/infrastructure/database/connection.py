import sqlite3
from pathlib import Path


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, timeout=10)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    version = connection.execute("PRAGMA user_version").fetchone()[0]
    if version > 1:
        connection.close()
        raise RuntimeError("Databáze pochází z novější verze aplikace.")
    if version == 0:
        migration = Path(__file__).parent / "migrations/001_initial.sql"
        try:
            connection.executescript("BEGIN IMMEDIATE;\n" + migration.read_text(encoding="utf-8")
                                     + "\nPRAGMA user_version = 1;\nCOMMIT;")
        except Exception:
            connection.rollback()
            connection.close()
            raise
    return connection
