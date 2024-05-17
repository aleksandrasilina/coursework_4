from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    def __init__(self, file_worker: str):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """Метод для загрузки списка вакансий с API сервиса с вакансиями"""
        pass
