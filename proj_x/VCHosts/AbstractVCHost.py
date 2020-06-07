from abc import ABC
from abc import abstractmethod


class AbstractVCHost(ABC):

    def __init__(self, config, api_key=None) -> None:
        self.config = config
        if api_key is None:
            # TODO: check for env var here and throw exception if its not there
            pass
        super().__init__()

    @abstractmethod
    def new_issue(self, title: str, tag: str, content: str) -> int:
        pass

    def __repr__(self):
        return f"{type(self)}(config={self.config})"
