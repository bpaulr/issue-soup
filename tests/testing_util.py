from pathlib import Path

from typing import List

import os

TEST_TEMP_LOC = "temp"


def create_test_temp_folder(loc: str) -> None:
    if not os.path.exists(loc):
        Path(loc).mkdir(parents=True, exist_ok=True)


def create_files_for_label_tests(loc: str) -> List[str]:
    file1 = """# Program make a simple calculator

# ToDo: implement a square function


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y\n"""
    create_test_temp_folder(TEST_TEMP_LOC)

    with open(os.path.join(TEST_TEMP_LOC, "file1.py"), "w+") as file:
        file.write(file1)

    return [os.path.join(TEST_TEMP_LOC, "file1.py")]


if __name__ == '__main__':
    create_files_for_label_tests(TEST_TEMP_LOC)
