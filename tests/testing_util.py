from pathlib import Path

import os


def create_test_temp_folder(loc: str) -> None:
    if not os.path.exists(loc):
        Path(loc).mkdir(parents=True, exist_ok=True)
