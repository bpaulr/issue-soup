from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='issue-soup',
    version='0.0.1',
    description='A package for creating version control issues, with custom labels/tags, from in-line code comments.',
    long_description=long_description,
    author='Bradley Read',
    author_email='bradleypaulread@gmail.com',
    url="https://github.com/bradleypaulread/issue-soup",
    packages=['issue_soup'],
    install_requires=[
        "requests",
        "pyyaml",
    ],
    scripts=[
        "scripts/nuke_issues.py",
    ]
)
