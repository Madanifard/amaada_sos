from abc import ABC, abstractmethod


class InsuredStrategy(ABC):

    @abstractmethod
    def insured_process(self, data):
        ...
