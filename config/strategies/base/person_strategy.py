from abc import ABC, abstractmethod


class PersonStrategy(ABC):

    @abstractmethod
    def person_process(self, data):
        ...
