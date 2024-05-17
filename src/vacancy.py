from typing import Self
from src.currency_converter_erapi import CurrencyConverterERAPI
from src.head_hunter_api import HeadHunterAPI


class Vacancy:
    """Класс для сохранения информации о вакансии"""

    def __init__(
            self,
            id: str,
            name: str,
            area: str,
            url: str,
            employer: str,
            requirement: str,
            responsibility: str,
            experience: str,
            employment: str,
            salary=None):
        """Конструктор вакансии"""
        self.id = id
        self.name = name
        self.area = area
        self.url = url
        self.employer = employer
        self.requirement = requirement
        self.responsibility = responsibility
        self.experience = experience
        self.employment = employment
        # зарплата является числом после выгрузки вакансий из файла
        if not isinstance(salary, int):
            # если зарплата не указана, то приравниваем ее к 0
            if salary:
                # за зарплату принимаем нижнюю границу диапазона
                if salary.get("from"):
                    self.__salary = salary.get("from")
                    self.salary_currency = salary.get("currency")
                    self.salary_gross = salary.get("gross")
                    # если зарплата указана с учетом НДФЛ, то пересчитываем без учета налога как в большинстве вакансий
                    self.__salary = self.get_salary_without_tax()
                    # конвертируем зарплату в рубли если зарплата указана в другой валюте
                    # self.__salary = self.convert_to_rubles()
                else:
                    self.__salary = 0
            else:
                self.__salary = 0
        else:
            self.__salary = salary

    def __str__(self):
        """Возвращает строковое представление о вакансии"""
        return (f'id вакансии: {self.id}\n'
                f'Название вакансии: {self.name}\n'
                f'Регион: {self.area}\n'
                f'Ссылка на вакансию: {self.url}\n'
                f'Зарплата: {self.__salary}\n'
                f'Работодатель: {self.employer}\n'
                f'Требования: {self.requirement}\n'
                f'Обязанности: {self.responsibility}\n'
                f'Опыт работы: {self.experience}\n'
                f'Занятость: {self.employment}\n'
                )

    def __repr__(self):
        """Возвращает строковое представление о вакансии"""
        return (f'id вакансии: {self.id}\n'
                f'Название вакансии: {self.name}\n'
                f'Регион: {self.area}\n'
                f'Ссылка на вакансию: {self.url}\n'
                f'Зарплата: {self.__salary}\n'
                f'Работодатель: {self.employer}\n'
                f'Требования: {self.requirement}\n'
                f'Обязанности: {self.responsibility}\n'
                f'Опыт работы: {self.experience}\n'
                f'Занятость: {self.employment}\n'
                )

    def __dict__(self) -> dict:
        """Возвращает словарь с атрибутами вакансии"""
        return dict(id=self.id,
                    name=self.name,
                    area=self.area,
                    url=self.url,
                    salary=self.__salary,
                    employer=self.employer,
                    requirement=self.requirement,
                    responsibility=self.responsibility,
                    experience=self.experience,
                    employment=self.employment
                    )

    def __gt__(self, other) -> bool:
        """Метод для сравнения зарплат вакансий"""
        if isinstance(other, self.__class__):
            return self.salary > other.salary
        elif isinstance(other, int):
            return self.salary > other

    @property
    def salary(self):
        """Геттер для вакансии"""
        return self.__salary

    @salary.setter
    def salary(self, salary):
        """Сеттер для вакансии"""
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.__salary = salary

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list[Self]:
        """Преобразует список вакансий из API сервиса с вакансиями в список экземпляров класса"""
        return [cls(**dict(id=vac.get('id'),
                           name=vac.get('name'),
                           area=vac.get('area').get('name'),
                           url=vac.get('alternate_url'),
                           employer=vac.get('employer').get('name'),
                           requirement=vac.get('snippet').get('requirement'),
                           responsibility=vac.get('snippet').get('responsibility'),
                           experience=vac.get('experience').get('name'),
                           employment=vac.get('employment').get('name'),
                           salary=vac.get('salary')
                           )
                    )
                for vac in vacancies
                ]

    def get_salary_without_tax(self) -> int:
        """Возвращает зарплату без учета НДФЛ"""
        if self.salary_gross:
            return round(self.__salary / 0.87)
        return self.__salary

    def convert_to_rubles(self) -> int:
        """Конвертирует зарплату в рубли"""
        # если валюта не в рублях
        if self.salary_currency != 'RUR':
            # приводим буквенный код валюты API сервиса с вакансиями к коду API сервиса конвертера валюты
            if self.salary_currency == 'BYR':
                self.salary_currency = 'BYN'
            cc_erapi = CurrencyConverterERAPI(self.salary_currency, self.__salary)
            return cc_erapi.convert_currency_erapi()
        return self.__salary
