from pathlib import Path
from typing import Dict
from urllib.parse import quote

import yaml

from issue_soup.VCHosts.AbstractVCHost import AbstractVCHost
from issue_soup.VCHosts.VCHostGitLab import VCHostGitLab

HOSTS = {
    "gitlab": VCHostGitLab,
    # ...
}


def dot_issuesoup_parser(file_path: Path, file_name: str = ".issue-soup.yaml") -> Dict[str, str]:
    config = {}

    with open(Path.joinpath(file_path, file_name), "r") as file:
        config = yaml.safe_load(file)

    # want all values as str/dict/list, can convert to int later on in VCHost if needed
    for k, v in config.items():
        if isinstance(v, int) or isinstance(v, float):
            config[k] = str(v)

    return config


def create_query(query_args: Dict[str, str]) -> str:
    query_args = [k + "=" + quote(v) for k, v in query_args.items()]
    return "?" + '&'.join(query_args)


def get_host(config: Dict[str, str]) -> AbstractVCHost:
    host_name = config["VCHOST"].strip().lower()
    if host_name in HOSTS:
        return HOSTS[host_name](config)
    return None
