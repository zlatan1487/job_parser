from abc import ABC, abstractmethod
from colorama import init, Fore


class AbstractSaver(ABC):
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def print_vacancies(vacancies, salary):
        print(f'{Fore.YELLOW}НАЙДЕНО {len(vacancies)} ВАКАНСИЙ С ОКЛАДОМ ОТ {salary} РУБ.')
        for vacancy in vacancies:
            print(f'{Fore.LIGHTWHITE_EX}title:', f'{Fore.GREEN}', vacancy['title'])
            print(f'{Fore.LIGHTWHITE_EX}link:', f'{Fore.GREEN}', vacancy['link'])
            print(f'{Fore.LIGHTWHITE_EX}salary:', f'{Fore.GREEN}', vacancy['salary'])
            print(f'{Fore.LIGHTWHITE_EX}description:', f'{Fore.GREEN}', vacancy['description'])
            print(f"{Fore.RED}{175 * '*'}")

        print(f'{Fore.YELLOW}НАЙДЕНО {len(vacancies)} ВАКАНСИЙ С ОКЛАДОМ ОТ {salary} РУБ.')

    @abstractmethod
    def add_vacancy(self, vacancy_data):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary_range):
        pass



