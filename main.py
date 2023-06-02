from classes.class_platforms import HeadHunterAPI, SuperJobAPI
from classes.class_json_save import JSONSaver
from utils.utils import get_vacancy_function


# передача данных от классов платформ в переменные
hh_api = HeadHunterAPI()
job_api = SuperJobAPI()

# выбор вакансий по ключевому слову
search_name_vacancy = input('выберите вакансию по ключевому слову например:[javascript, python, erlang, java, стоматолог]: ').strip()

# вызов метода классов [HeadHunterAPI, SuperJobAPI] get_vacancies для получения вакансий
get_hh_vacancy = hh_api.get_vacancies(search_name_vacancy)
get_job_vacancy = job_api.get_vacancies(search_name_vacancy)
type(get_hh_vacancy)

# вызов функции "get_vacancy_function" из файла utils в которой создаеться экземпляр класса Vacancy для платформ
example_vacancy_hh = get_vacancy_function(get_hh_vacancy)
example_vacancy_job = get_vacancy_function(get_job_vacancy)


# создание экземпляров класса JSONSaver для платформ с параметром [путь к файлу vacancies.json в котором будут храниться вакансии из платформ]
json_saver_hh = JSONSaver('json/vacancies.json')
json_saver_job = JSONSaver('json/vacancies.json')


# вызов метода экземпляров класса класса JSONSaver для добавления вакансий
json_saver_hh.add_vacancy(example_vacancy_hh)
json_saver_job.add_vacancy(example_vacancy_job)


def user_interaction():
    """
    функция осуществляет взаимодействие с пользователем
    """

    search_salary = input('поиск вакансий, укажите зарплату (от...): ')

    try:
        search_salary = int(search_salary)
    except ValueError:
        print("Ошибка: Введите целое число в качестве зарплаты.")
        exit()

    # Проверяем, является ли введенная зарплата положительным числом
    if search_salary <= 0:
        print("Ошибка: Зарплата должна быть положительным числом.")
        exit()

    # Если все проверки пройдены успешно, можно продолжить выполнение программы
    print(f"Вы указали зарплату: {search_salary}")

    json_saver_hh.get_vacancies_by_salary(search_salary)


if __name__ == "__main__":
    user_interaction()

