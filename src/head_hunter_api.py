from src.parser import Parser
import requests


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self, file_worker: str):
        """Конструктор для API HeadHunter"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword: str):
        """Метод для загрузки списка вакансий с API HeadHunter"""
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1

    @property
    def url(self):
        """Геттер для url"""
        return self.__url

    @property
    def headers(self):
        """Геттер для headers"""
        return self.__headers

    @property
    def params(self):
        """Геттер для params"""
        return self.__params

    @property
    def vacancies(self):
        """Геттер для списка вакансий"""
        return self.__vacancies

    @property
    def file_worker(self):
        """Геттер для имени файла"""
        return self._file_worker

    @file_worker.setter
    def file_worker(self, file_worker):
        """Геттер для имени файла"""
        self._file_worker = file_worker
