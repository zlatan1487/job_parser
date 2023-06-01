from abc import ABC, abstractmethod


class AbstractJobSiteAPI(ABC):
    """
        абстрактный класс для работы с апи платформ
    """
    @abstractmethod
    def get_vacancies(self, keyword):
        pass
