from src.vacancy import Vacancy


def get_vacancies_by_salary(vacancies: list[Vacancy], salary_from: str = None) -> list[Vacancy]:
    """Возвращает список вакансий, зарплата которых выше или равна salary_from"""
    if salary_from:
        if salary_from.isdigit():
            return list(filter(lambda x: x.salary >= int(salary_from), vacancies))
        raise ValueError("Некорректно указана зарплата")
    return vacancies


def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    """Сортирует вакансии в порядке уменьшения зарплаты"""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: list[Vacancy], top_n: str = None) -> list[Vacancy]:
    """Возвращает топ n вакансий"""
    if top_n:
        if top_n.isdecimal():
            return vacancies[:int(top_n)]
        raise ValueError("Некорректно указан топ N вакансий")
    return vacancies

def print_vacancies(vacancies: list[Vacancy]):
    """Выводит список вакансий в консоль"""
    for vacancy in vacancies:
        print(vacancy)
