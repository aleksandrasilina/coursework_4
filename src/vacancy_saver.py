from abc import ABC, abstractmethod


class VacancySaver(ABC):
    """Абстрактный класс для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях
    """

    @abstractmethod
    def add_vacancies(self, vacancies):
        """Метод для сохранения списка экземпляров вакансий в файл"""
        pass

    @abstractmethod
    def filter_vacancies(self, *args, **kwargs):
        """Метод для получения вакансий из файла по указанным критериям"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Метод для удаления вакансии из файла"""
        pass
