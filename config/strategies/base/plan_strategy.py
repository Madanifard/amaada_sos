from abc import ABC, abstractmethod


class PlanStrategy(ABC):

    @abstractmethod
    def plan_process(self, data):
        ...
