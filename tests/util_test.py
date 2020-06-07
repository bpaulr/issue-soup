import os
import pathlib

import pytest

from proj_x.util import dot_projx_parser


@pytest.mark.parametrize("content_str,expected", [
    ('\n'.join([
        "VCHOST: gitlab",
        "PROJECT_ID: 19212576",
    ]), {
         "VCHOST": "gitlab",
         "PROJECT_ID": "19212576",
     }),
    ('\n'.join([
        "VCHOST: gitlab",
        "PROJECT_ID: 19212576",
        "labels: \n \
            - test1 \n \
            - test2 \n \
            - test3 \n \
            - test4 \n \
            - test5",
    ]), {
        "VCHOST": "gitlab",
        "PROJECT_ID": "19212576",
        "labels": ["test1", "test2", "test3", "test4", "test5"],
     }),
])
def test_dot_projx_parser(content_str, expected):
    path = str(pathlib.Path(__file__).parent.absolute()) + "/resources/temp/"
    file_name = ".proj_x.yaml"

    if not os.path.exists(path):
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    with open(path + file_name, "w+") as file:
        file.write(content_str)

    assert dot_projx_parser(path, file_name) == expected
