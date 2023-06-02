import re


class Vacancy:

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

    def compare_salary(self, other_employee):
        if self.salary > other_employee.salary:
            return f"{self.link}'s salary is higher than {other_employee.link}'s salary."
        elif self.salary < other_employee.salary:
            return f"{self.link}'s salary is lower than {other_employee.link}'s salary."
        else:
            return f"{self.link}'s salary is equal to {other_employee.link}'s salary."

