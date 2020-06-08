import os
from pathlib import Path
from typing import List
from typing import Set
from typing import Tuple

LABEL_SUFFIX = ':'


def find_labels(project_root: Path, labels: List[str]) -> List[Tuple[str, str, int]]:
    """
    Look though all *.py files from the project root for lines with given labels.

    :param project_root: path of the project root
    :param labels: List of labels to be looking for
    :return: List of tuples in the form (file, label, line_num)
    """
    files = list(Path(project_root).rglob("*.[pP][yY]"))
    found_labels = []
    for file in files:
        _found_labels = find_label(file, set(labels))
        if not _found_labels:
            continue
        for _ in _found_labels:
            label, line_num = _
            found_labels.append((file, label, line_num))
    return found_labels


def find_label(file: Path, labels: Set[str]) -> List[Tuple[str, int]]:
    """
    Check a file's lines and find labels.

    :param file: file to search
    :param labels: Labels to be looking for
    :return: List of tuples of the form (label, line_num) for found labels
    """
    file_path = os.fspath(file)
    found_labels = []
    with open(file_path, "r") as file:
        line = file.readline()
        line_num = 1
        while line and line != "":
            for label in labels:
                if label + LABEL_SUFFIX in line:
                    found_labels.append((label, line_num))
                    break
            line = file.readline()
            line_num += 1
    return found_labels


def get_label_block(file: Path, line_start: int) -> Tuple[str, str]:
    """
    Get the block of text associated with a label.

    :param file: File where the label is in
    :param line_start: Line that the label is on
    :return: Tuple of the form (first line of block, full text of label block)
    """
    with open(os.fspath(file), "r") as file:
        # skip to line before the line we want
        for _ in range(line_start-1):
            file.readline()
        block = []
        first_line = line = file.readline().strip()
        while line.strip().startswith("#"):
            block.append(line)
            line = file.readline().strip()
        return first_line.replace("#", "").strip(), ''.join(block).replace("#", "").strip()
