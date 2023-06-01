from abstract_classes.abstract_job_site_api import AbstractJobSiteAPI
from mixin.mixin import Path
import requests


class HeadHunterAPI(AbstractJobSiteAPI):
    def get_vacancies(self, keyword, per_page=100):
        vacancies_hh = []
        if keyword == '':
            print(f'empty line for {self.__class__.__name__[:-3]}.')
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
                    print(f"Error occurred while fetching vacancies for page {page}")

        else:
            print("Error occurred while fetching vacancies.")

        return vacancies_hh


class SuperJobAPI(AbstractJobSiteAPI, Path):

    def get_vacancies(self, keyword, page=None):
        vacancies_job = []
        if keyword == '':
            print(f'empty line for {self.__class__.__name__[:-3]}.')
            return vacancies_job

        else:
            url = 'https://api.superjob.ru/2.0/vacancies/'
            params = {
                'keyword': keyword,
                'app_key': self.private_key,
                'page': page,
            }

            response = requests.get(url, params=params)
            data = response.json()

            if not data['objects']:
                print('empty')
            for vacancy in data.get('objects', []):
                title = vacancy.get('profession', '')
                link = vacancy.get('link', '')
                salary = vacancy.get('payment_from', '')
                description = vacancy.get('vacancyRichText', '')
                vacancies_job.append({'title': title, 'link': link, 'salary': salary, 'description': description})

            return vacancies_job


