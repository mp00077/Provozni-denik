from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    data_dir: Path

    @property
    def database_path(self) -> Path:
        return self.data_dir / "denik.sqlite3"
