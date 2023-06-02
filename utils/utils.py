from classes.vacansy import Vacancy


def get_vacancy_function(value):
    """Функция помещает указанные элементы в поля класса в класс Vacancy,
    методы повышения класса для проверки и сравнения зарплаты вакансий на разных платформах,
    сохраненные вакансии и сохраненные в vacancy_list
    :param: список с вакансиями
    :return: список выбранных заданий
    """
    vacancy_list = []
    for res in value:
        v = Vacancy(res['title'], res['link'], res['salary'], res['description'])
        v.find_salary()
        v.validate_description()
        vacancy_list.append({'title': v.title, 'link': v.link, 'salary': v.salary, 'description': v.description})
    return vacancy_list
