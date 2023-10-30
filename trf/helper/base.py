from abc import ABC, abstractmethod
from .driver import Driver


class BaseClass(ABC):
    _url_base = None

    def __init__(self, headless: bool, driver_name: str):
        self.driver = Driver(headless, driver_name)

    def __call__(self) -> Driver:
        return self.driver

    @property
    def url_base(self) -> str:
        return self._url_base

    @abstractmethod
    def execute(self) -> None:
        pass
