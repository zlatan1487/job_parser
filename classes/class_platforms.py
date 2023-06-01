from abstract_classes.abstract_job_site_api import AbstractJobSiteAPI
from mixin.mixin import Path


class HeadHunterAPI(AbstractJobSiteAPI):
    def get_vacancies(self, keyword):
        pass


class SuperJobAPI(AbstractJobSiteAPI, Path):
    def get_vacancies(self, keyword):
        pass
