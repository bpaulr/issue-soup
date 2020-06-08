from pathlib import Path

import pytest

from proj_x.labels import find_labels
from proj_x.labels import get_label_block
from tests.testing_util import create_files_for_label_tests

TEST_TEMP_LOC = str(Path.joinpath(Path(__file__).parent.absolute(), "temp"))

create_files_for_label_tests(TEST_TEMP_LOC)


def test_find_labels():
    from operator import itemgetter

    root = Path(TEST_TEMP_LOC)
    labels = ["Feature", "ToDo", "Bug"]

    # sort by line number as set use messes up ordering
    expected = sorted([
        (Path.joinpath(root, "file1.py"), "ToDo", 3),
        (Path.joinpath(root, "file1.py"), "Bug", 6),
        (Path.joinpath(root, "file2.py"), "Feature", 19),
    ], key=itemgetter(2))
    print(sorted(find_labels(root, labels), key=itemgetter(2)))
    assert sorted(find_labels(root, labels), key=itemgetter(2)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ((Path.joinpath(Path(TEST_TEMP_LOC), "file1.py"), 3), ("ToDo: make into Calculator object", "ToDo: make into Calculator object")),
    ((Path.joinpath(Path(TEST_TEMP_LOC), "file1.py"), 6), ("Bug: add function adds negative y,", "Bug: add function adds negative y, need to investigate in the future as this is a critical bug")),
    ((Path.joinpath(Path(TEST_TEMP_LOC), "file2.py"), 19), ("Feature: implement a square function", "Feature: implement a square function so the user can square without having to use the multiply function")),
])
def test_get_label_block(test_input, expected):
    print(test_input)
    print(get_label_block(test_input[0], test_input[1]))
    assert get_label_block(test_input[0], test_input[1]) == expected


if __name__ == '__main__':
    test_get_label_block((Path.joinpath(Path(TEST_TEMP_LOC), "file1.py"), 6), ("Bug: add function adds negative y,", "Bug: add function adds negative y, need to investigate in the future as this is a critical bug"))
