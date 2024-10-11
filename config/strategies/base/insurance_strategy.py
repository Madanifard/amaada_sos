from abc import ABC, abstractmethod


class InsuranceStrategy(ABC):

    @abstractmethod
    def insurance_process(self, data):
        ...
