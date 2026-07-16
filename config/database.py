import sqlite3
from pathlib import Path

from config.config import CONFIG


def get_connection(database_path: Path | None = None) -> sqlite3.Connection:
    path = database_path or CONFIG.database_path
    path.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(path)
