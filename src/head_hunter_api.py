from src.parser import Parser
import requests


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self, file_worker: str):
        """Конструктор для API HeadHunter"""
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword: str):
        """Метод для загрузки списка вакансий с API HeadHunter"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
