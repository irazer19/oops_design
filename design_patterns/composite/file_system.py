from abc import ABC, abstractmethod


class Filesystem(ABC):
    @abstractmethod
    def ls(self):
        pass
