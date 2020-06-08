import os
from pathlib import Path
from typing import List


def create_test_temp_folder(loc: str) -> None:
    if not os.path.exists(loc):
        Path(loc).mkdir(parents=True, exist_ok=True)


def create_files_for_label_tests(loc: str) -> List[str]:
    file1 = """# Program make a simple calculator

# ToDo: make into Calculator object


# Bug: add function adds negative y,
# need to investigate in the future as this is a critical
# bug

# This function adds two numbers
def add(x, y):
    return x + -y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y\n"""

    file2 = """# Program make a simple calculator


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# Feature: implement a square function
# so the user can square without having
# to use the multiply function


# This function divides two numbers
def divide(x, y):
    return x / y\n"""

    create_test_temp_folder(loc)

    files = [
        ("file1.py", file1),
        ("file2.py", file2),
    ]

    for file_name, content in files:
        with open(Path.joinpath(Path(loc), file_name), "w+") as file:
            file.write(content)

    return [Path.joinpath(Path(loc), file[0]) for file in files]
