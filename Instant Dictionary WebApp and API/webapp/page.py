

# this file is the abstract class for all pages

from abc import ABC, abstractmethod

class Page(ABC):
    @abstractmethod
    def serve(self, req):
        pass


