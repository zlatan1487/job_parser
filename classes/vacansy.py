import re


class Vacancy:

    """class for working with vacancies"""
    """класс по работе с вакансиями"""

    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __eq__(self, other):
        return self.salary == other.salary

    def find_salary(self):
        if self.salary is None:
            self.salary = 0
        else:
            if isinstance(self.salary, dict):
                self.salary = self.salary.get('from', self.salary.get('payment_from', 0))
            else:
                self.salary = self.salary
        return self.salary

    @staticmethod
    def strip_tags(html_text):
        clean_text = re.sub('<.*?>', '', html_text)
        return clean_text

    def validate_description(self):
        if self.description is not None:
            self.description = self.strip_tags(self.description)
            self.description = self.description[:200]
            self.description += '...'
        return self.description
