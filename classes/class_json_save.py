import json
import os
from abstract_classes.abstract_saver import AbstractSaver


class JSONSaver(AbstractSaver):
    """
    класс для работы с файлом json
    """
    def __init__(self, filename):
        super().__init__(filename)

    def add_vacancy(self, vacancy_data):

        if not vacancy_data:
            return

        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            data = {'vacancies': []}
        else:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

        vacancies = data["vacancies"]

        existing_vacancies = set(tuple(vacancy.items()) for vacancy in vacancies)

        write_to_file = False

        for vacancy_dict in vacancy_data:
            vacancy_tuple = tuple(vacancy_dict.items())
            if vacancy_tuple not in existing_vacancies:
                vacancies.append(vacancy_dict)
                existing_vacancies.add(vacancy_tuple)
                write_to_file = True

        if write_to_file:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        else:
            print(f'Аналогичные вакансии уже записаны в JSON файл')

    def get_vacancies_by_salary(self, salary_range):

        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            print('Файл пустой.')
            return []
        with open(self.filename, encoding='utf-8') as file:
            data = json.load(file)

        vacancies = []
        json_list = data['vacancies']

        if isinstance(json_list, list):
            for vacancy_list in data['vacancies']:
                if isinstance(vacancy_list, dict) and 'salary' in vacancy_list:
                    salary = vacancy_list['salary']
                    if salary == salary_range:
                        vacancies.append(vacancy_list)
        else:
            print('Неверный формат данных.')

        if not vacancies:
            print('Вакансий не найдено')
        else:
            self.print_vacancies(vacancies, salary_range)
        return vacancies


