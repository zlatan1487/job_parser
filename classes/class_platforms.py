from abstract_classes.abstract_job_site_api import AbstractJobSiteAPI
from mixin.mixin import Path
import requests


class HeadHunterAPI(AbstractJobSiteAPI):
    def get_vacancies(self, keyword, per_page=100):
        vacancies_hh = []
        if keyword == '':
            print(f'пустая строка для {self.__class__.__name__[:-3]}.')
            return vacancies_hh

        url = f'https://api.hh.ru/vacancies'

        params = {
            'enable_snippets': 'true',
            'text': keyword,
            'area': '2',
            'page': '1',
            'per_page': str(per_page)
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            total_pages = data['pages']

            for page in range(1, total_pages + 1):
                params['page'] = str(page)
                response = requests.get(url, params=params)
                data = response.json()

                if response.status_code == 200:

                    for vacancy in data.get('items', []):
                        title = vacancy.get('name', '')
                        link = vacancy.get('alternate_url', '')
                        salary = vacancy.get('salary')
                        description = vacancy.get('snippet', {}).get('responsibility', '')
                        vacancies_hh.append({'title': title, 'link': link, 'salary': salary, 'description': description})

                else:
                    print(f"Ошибка при получении вакансий для страницы")

        else:
            print("Ошибка при получении вакансий.")
        print(f'найдено {len(vacancies_hh)} вакансий на платформы hh.ru')
        return vacancies_hh


class SuperJobAPI(AbstractJobSiteAPI, Path):

    def get_vacancies(self, keyword):
        vacancies_job = []
        if keyword == '':
            print(f'пустая строка для {self.__class__.__name__[:-3]}.')
            return vacancies_job

        else:
            url = 'https://api.superjob.ru/2.0/vacancies/'
            params = {
                'keyword': keyword,
                'app_key': self.private_key,
                'page': 0,
            }

            while True:
                response = requests.get(url, params=params)
                data = response.json()
                try:
                    if not data['objects']:
                        break
                except KeyError:
                    print("Ошибка: непредвиденный формат ответа от SuperJob API.")
                    break

                for vacancy in data['objects']:
                    title = vacancy.get('profession', '')
                    link = vacancy.get('link', '')
                    salary = vacancy.get('payment_from', '')
                    description = vacancy.get('vacancyRichText', '')
                    vacancies_job.append({'title': title, 'link': link, 'salary': salary, 'description': description})

                if 'more' in data:
                    params['page'] += 1
                else:
                    break
            print(f'найдено {len(vacancies_job)} вакансий на платформы super job.ru')
            return vacancies_job

