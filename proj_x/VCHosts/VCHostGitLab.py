from proj_x.VCHosts.AbstractVCHost import AbstractVCHost

from proj_x.util import create_query
import requests
from os import getenv

API_URL = "https://gitlab.com/api/v4/"
ISSUE_URL = API_URL + "projects/{}/issues"


class VCHostGitLab(AbstractVCHost):

    def new_issue(self, title: str, tag: str, content: str) -> int:
        project_url = self.__get_project_url()
        query_args = {
            "title": title,
            "label": tag,
            "description": content,
        }
        issue_query = create_query(query_args)
        response = requests.post(project_url + issue_query, headers={"PRIVATE-TOKEN": getenv("API_KEY")})
        return response.json()["iid"]

    def __get_project_url(self) -> str:
        return ISSUE_URL.format(self.config["PROJECT_ID"])
