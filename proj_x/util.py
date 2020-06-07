from typing import Dict
import yaml
from urllib.parse import quote


def dot_projx_parser(file_path: str, file_name: str = ".proj_x.yaml") -> Dict[str, str]:
    config = {}

    with open(file_path + "/" + file_name, "r") as file:
        config = yaml.safe_load(file)

    # want all values as str/dict/list, can convert to int later on in VCHost if needed
    for k, v in config.items():
        if isinstance(v, int) or isinstance(v, float):
            config[k] = str(v)

    return config


def create_query(query_args: Dict[str, str]) -> str:
    query_args = [k + "=" + quote(v) for k, v in query_args.items()]
    return "?" + '&'.join(query_args)
