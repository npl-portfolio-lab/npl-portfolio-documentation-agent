from pathlib import Path

import yaml


def load_project(file_path: Path) -> dict:
    with file_path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return data.get("project", {})
