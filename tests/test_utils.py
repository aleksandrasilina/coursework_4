from src import utils


def test_utils_get_vacancies_by_salary(vacancy_1, vacancy_2, vacancy_3):
    """Тестирует метод для фильтрации списка вакансий по зарплате"""
    vacancies_list = [vacancy_1, vacancy_2, vacancy_3]
    assert utils.get_vacancies_by_salary(vacancies_list, 20000) == [vacancy_2, vacancy_3]


def test_utils_sort_vacancies(vacancy_1, vacancy_2, vacancy_3):
    """Тестирует метод для сортировки вакансий в порядке уменьшения зарплаты"""
    vacancies_list = [vacancy_1, vacancy_2, vacancy_3]
    assert utils.sort_vacancies(vacancies_list) == [vacancy_3, vacancy_2, vacancy_1]


def test_utils_get_top_vacancies(vacancy_1, vacancy_2, vacancy_3):
    """Тестирует метод для получения топа n вакансий"""
    vacancies_list = [vacancy_3, vacancy_2, vacancy_1]
    assert utils.get_top_vacancies(vacancies_list, 2) == [vacancy_3, vacancy_2]


def test_utils_print_vacancies(vacancy_1, vacancy_2, capsys):
    """Тестирует метод для вывода списка вакансий в консоль"""
    vacancies_list = [vacancy_1, vacancy_2]
    utils.print_vacancies(vacancies_list)
    captured = capsys.readouterr()
    assert captured.out == ('id вакансии: 1\n'
                            'Название вакансии: Test_1\n'
                            'Регион: Test_1\n'
                            'Ссылка на вакансию: Test_1\n'
                            'Зарплата: 0\n'
                            'Работодатель: Test_1\n'
                            'Требования: Test_1\n'
                            'Обязанности: Test_1\n'
                            'Опыт работы: Test_1\n'
                            'Занятость: Test_1\n\n'
                            'id вакансии: 2\n'
                            'Название вакансии: Test_2\n'
                            'Регион: Test_2\n'
                            'Ссылка на вакансию: Test_2\n'
                            'Зарплата: 50000\n'
                            'Работодатель: Test_2\n'
                            'Требования: Test_2\n'
                            'Обязанности: Test_2\n'
                            'Опыт работы: Test_2\n'
                            'Занятость: Test_2\n\n')
