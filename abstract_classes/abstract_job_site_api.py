from abc import ABC, abstractmethod


class AbstractJobSiteAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass
