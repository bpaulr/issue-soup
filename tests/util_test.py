import json
import os
from pathlib import Path

import pytest

from label_soup.util import create_query
from label_soup.util import dot_labelsoup_parser
from tests.testing_util import create_test_temp_folder

TEST_TEMP_LOC = str(Path.joinpath(Path(__file__).parent.absolute(), "temp"))


@pytest.mark.parametrize("content_str,expected", [
    # 1st test
    ('\n'.join([
        "VCHOST: gitlab",
        "PROJECT_ID: 19212576",
    ]), {
         "VCHOST": "gitlab",
         "PROJECT_ID": "19212576",
     }),
    # 2nd test
    ("""VCHOST: gitlab
PROJECT_ID: 19212576
LABELS:
  foo:
    description: foo123
    color_hex: ffff00
  bar:
    description: bar123
    color_hex: 008000
  ToDo:
    description: ToDo123
    color_hex: e9e
  Feature:
    description: Feature123
    color_hex: FF0000""", {
        "VCHOST": "gitlab",
        "PROJECT_ID": "19212576",
        "LABELS": {
            "foo": {
                "description": "foo123",
                "color_hex": "ffff00",
            },
            "bar": {
                "description": "bar123",
                "color_hex": "008000",
            },
            "ToDo": {
                "description": "ToDo123",
                "color_hex": "e9e",
            },
            "Feature": {
                "description": "Feature123",
                "color_hex": "FF0000",
            },
        },
    }),
])
def test_dot_labelsoup_parser(content_str, expected):
    create_test_temp_folder(TEST_TEMP_LOC)

    with open(os.path.join(TEST_TEMP_LOC, ".label-soup.yaml"), "w+") as file:
        file.write(content_str)
    print(json.dumps(dot_labelsoup_parser(Path(TEST_TEMP_LOC), ".label-soup.yaml"), sort_keys=True, indent=2))
    print(json.dumps(expected, sort_keys=True, indent=2))
    print()
    assert json.dumps(dot_labelsoup_parser(Path(TEST_TEMP_LOC), ".label-soup.yaml"), sort_keys=True) \
           == json.dumps(expected, sort_keys=True)


@pytest.mark.parametrize("test_input,expected", [
    ({
         "title": "this is a title",
         "description": "this is a description",
     }, "?title=this%20is%20a%20title&description=this%20is%20a%20description"),
])
def test_create_query(test_input, expected):
    assert create_query(test_input) == expected
