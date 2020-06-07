from os import getenv

import requests

import proj_x.util
from proj_x.VCHosts.AbstractVCHost import AbstractVCHost

API_URL = "https://gitlab.com/api/v4/"
PROJECT_URL = API_URL + "projects/{}/"
LABEL_URL = PROJECT_URL + "labels/"
ISSUE_URL = PROJECT_URL + "issues/"


class VCHostGitLab(AbstractVCHost):

    def create_labels(self) -> int:
        labels = self.config["LABELS"]
        label_url = self.__get_url(LABEL_URL)
        for label in labels:
            label_query = proj_x.util.create_query({
                "name": label.strip().lower(),
                "color": "#FFAABB",
            })
            requests.post(label_url + label_query, headers={"PRIVATE-TOKEN": getenv("API_KEY")})

    def new_issue(self, title: str, tag: str, content: str) -> int:
        issue_url = self.__get_url(ISSUE_URL)
        query_args = {
            "title": title,
            "label": tag,
            "description": content,
        }
        issue_query = proj_x.util.create_query(query_args)
        response = requests.post(issue_url + issue_query, headers={"PRIVATE-TOKEN": getenv("API_KEY")})
        return response.json()["iid"]

    def __get_url(self, url: str) -> str:
        return url.format(self.config["PROJECT_ID"])
