from src.vacancy_saver import VacancySaver
from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy

import os.path
import json


class JSONSaver(VacancySaver):
    """Класс для сохранения вакансий из сервиса с вакансиями в файл формата JSON"""

    def __init__(self, hh_api: HeadHunterAPI):
        """Конструктор для сохранения вакансий в файл"""
        self.file_name = hh_api.file_worker + '.json'

    def add_vacancies(self, vacancies: list[Vacancy]):
        """Метод для сохранения списка экземпляров вакансий в файл"""
        with open(os.path.join('..', 'data', self.file_name), 'w', encoding='utf-8') as file:
            vacancies_list = [vac.__dict__() for vac in vacancies]
            json.dump(vacancies_list, file, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> list[dict]:
        """Возвращает содержимое файла"""
        with open(os.path.join('..', 'data', self.file_name), 'r', encoding='utf-8') as file:
            return json.load(file)

    def filter_vacancies(self, keywords: list[str]) -> list[Vacancy]:
        """Метод для получения вакансий из файла по указанным критериям"""
        filter_vacancies = []
        for vac in self.get_vacancies():
            if all(
                    any(
                        word.lower() in value.lower() for value in vac.values()
                        if value and not isinstance(value, int)
                    )
                    for word in keywords
            ):
                filter_vacancies.append(vac)
        return [Vacancy(**vac) for vac in filter_vacancies]

    def add_vacancy(self, vacancy: Vacancy):
        """Метод для добавления вакансии в файл"""
        vacancies_data = self.get_vacancies()
        vacancies_data.append(vacancy.__dict__())
        with open(os.path.join('..', 'data', self.file_name), 'w', encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy):
        """Метод для удаления вакансии из файла"""
        vacancies_data = self.get_vacancies()
        for vac in vacancies_data:
            if vac['id'] == vacancy.id:
                vacancies_data.remove(vac)
        with open(os.path.join('..', 'data', self.file_name), 'w', encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False, indent=4)
