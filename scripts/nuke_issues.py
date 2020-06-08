import sys
from os import getenv

import requests

PROJECT_ID = "19212576"
API_URL = "https://gitlab.com/api/v4/"
PROJECT_URL = API_URL + "projects/{}/"
LABEL_URL = PROJECT_URL + "labels/"
ISSUE_URL = PROJECT_URL + "issues/"


def nuke_issues_and_labels(api_key: str = getenv["API_KEY"]) -> None:
    issue_response = requests.get(ISSUE_URL.format(PROJECT_ID) + "?per_page=100", headers={"PRIVATE-TOKEN": api_key})

    for response in issue_response.json():
        print("Deleting issue " + str(response["iid"]))
        print(requests.delete(ISSUE_URL.format(PROJECT_ID) + str(response["iid"]), headers={"PRIVATE-TOKEN": api_key}).status_code)
        print()

    labels_response = requests.get(LABEL_URL.format(PROJECT_ID), headers={"PRIVATE-TOKEN": api_key})

    for response in labels_response.json():
        print("Deleting label " + str(response["name"]))
        print(requests.delete(LABEL_URL.format(PROJECT_ID) + str(response["id"]), headers={"PRIVATE-TOKEN": api_key}).status_code)
        print()


if __name__ == '__main__':
    args = sys.argv
    if 1 < len(args) < 3:
        nuke_issues_and_labels(args[1])
    else:
        raise Exception("Invalid api key argument, usage `nuke_issues.py <API_KEY>`")
