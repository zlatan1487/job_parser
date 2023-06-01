from abc import ABC, abstractmethod


class AbstractSaver(ABC):
    """
       абстрактный класс для работы с файлом json
    """
    @abstractmethod
    def add_vacancy(self, vacancy_data):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary_range):
        pass
