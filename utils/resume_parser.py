from pathlib import Path


def parse_resume(file_path: str | Path) -> dict[str, str]:
    return {"text": "", "source": str(file_path)}
