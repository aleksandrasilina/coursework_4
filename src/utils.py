from src.vacancy import Vacancy


def get_vacancies_by_salary(vacancies: list[Vacancy], salary_from: int) -> list[Vacancy]:
    """Возвращает список вакансий, зарплата которых выше или равна salary_from"""
    return list(filter(lambda x: x.salary >= salary_from, vacancies))


def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    """Сортирует вакансии в порядке уменьшения зарплаты"""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Возвращает топ n вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies: list[Vacancy]):
    """Выводит список вакансий в консоль"""
    for vacancy in vacancies:
        print(vacancy)
