from os import getenv

import requests

import label_soup.util
from label_soup.VCHosts.AbstractVCHost import AbstractVCHost
from label_soup.color import parse_hex

API_URL = "https://gitlab.com/api/v4/"
PROJECT_URL = API_URL + "projects/{}/"
LABEL_URL = PROJECT_URL + "labels/"
ISSUE_URL = PROJECT_URL + "issues/"


class VCHostGitLab(AbstractVCHost):

    def create_labels(self) -> None:
        labels = self.config["LABELS"]
        label_url = self.__get_url(LABEL_URL)
        # Feature: allow all attributes from labels api to be specified in yaml
        for label, details in labels.items():
            label_query = label_soup.util.create_query({
                "name": label.strip(),
                "description": details["description"] if details["description"] is not None else "",
                "color": parse_hex(details["color_hex"]) if details["color_hex"] is not None else "#428BCA",
            })
            requests.post(label_url + label_query, headers={"PRIVATE-TOKEN": getenv("API_KEY")})

    def new_issue(self, title: str, label: str, content: str) -> int:
        issue_url = self.__get_url(ISSUE_URL)
        query_args = {
            "title": title,
            "labels": label,
            "description": content,
        }
        issue_query = label_soup.util.create_query(query_args)
        response = requests.post(issue_url + issue_query, headers={"PRIVATE-TOKEN": getenv("API_KEY")})
        return response.json()["iid"]

    def __get_url(self, url: str) -> str:
        return url.format(self.config["PROJECT_ID"])
