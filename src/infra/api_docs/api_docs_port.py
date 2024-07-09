from abc import ABC, abstractmethod

class APIDocsPort(ABC):
    @abstractmethod
    def setup(self, app):
        pass
