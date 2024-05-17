import pytest

from src.vacancy import Vacancy


def test_vacancy_init_without_salary(vacancy_1):
    """Тестирует конструктор вакансии без зарплаты"""
    assert vacancy_1.id == '1'
    assert vacancy_1.name == 'Test_1'
    assert vacancy_1.area == 'Test_1'
    assert vacancy_1.url == 'Test_1'
    assert vacancy_1.employer == 'Test_1'
    assert vacancy_1.requirement == 'Test_1'
    assert vacancy_1.responsibility == 'Test_1'
    assert vacancy_1.experience == 'Test_1'
    assert vacancy_1.employment == 'Test_1'
    assert vacancy_1.salary == 0


def test_vacancy_init_with_int_salary(vacancy_2):
    """Тестирует конструктор вакансии, где зарплата - число"""
    assert vacancy_2.id == '2'
    assert vacancy_2.name == 'Test_2'
    assert vacancy_2.area == 'Test_2'
    assert vacancy_2.url == 'Test_2'
    assert vacancy_2.employer == 'Test_2'
    assert vacancy_2.requirement == 'Test_2'
    assert vacancy_2.responsibility == 'Test_2'
    assert vacancy_2.experience == 'Test_2'
    assert vacancy_2.employment == 'Test_2'
    assert vacancy_2.salary == 50000


def test_vacancy_init_with_salary_from(vacancy_3):
    """Тестирует конструктор вакансии, где зарплата - словарь и есть значение salary['from']"""
    assert vacancy_3.id == '3'
    assert vacancy_3.name == 'Test_3'
    assert vacancy_3.area == 'Test_3'
    assert vacancy_3.url == 'Test_3'
    assert vacancy_3.employer == 'Test_3'
    assert vacancy_3.requirement == 'Test_3'
    assert vacancy_3.responsibility == 'Test_3'
    assert vacancy_3.experience == 'Test_3'
    assert vacancy_3.employment == 'Test_3'
    assert vacancy_3.salary == 180000


def test_vacancy_init_without_salary_from(vacancy_6):
    """Тестирует конструктор вакансии, где зарплата - словарь и нет значения salary['from']"""
    assert vacancy_6.id == '6'
    assert vacancy_6.name == 'Test_6'
    assert vacancy_6.area == 'Test_6'
    assert vacancy_6.url == 'Test_6'
    assert vacancy_6.employer == 'Test_6'
    assert vacancy_6.requirement == 'Test_6'
    assert vacancy_6.responsibility == 'Test_6'
    assert vacancy_6.experience == 'Test_6'
    assert vacancy_6.employment == 'Test_6'
    assert vacancy_6.salary == 0


def test_vacancy_str(vacancy_1):
    """Тестирует метод __str__ - строковое представление вакансии"""
    assert str(vacancy_1) == ('id вакансии: 1\n'
                              'Название вакансии: Test_1\n'
                              'Регион: Test_1\n'
                              'Ссылка на вакансию: Test_1\n'
                              'Зарплата: 0\n'
                              'Работодатель: Test_1\n'
                              'Требования: Test_1\n'
                              'Обязанности: Test_1\n'
                              'Опыт работы: Test_1\n'
                              'Занятость: Test_1\n')


def test_vacancy_repr(vacancy_2):
    """Тестирует метод __repr__ - строковое представление вакансии"""
    assert repr(vacancy_2) == ('id вакансии: 2\n'
                               'Название вакансии: Test_2\n'
                               'Регион: Test_2\n'
                               'Ссылка на вакансию: Test_2\n'
                               'Зарплата: 50000\n'
                               'Работодатель: Test_2\n'
                               'Требования: Test_2\n'
                               'Обязанности: Test_2\n'
                               'Опыт работы: Test_2\n'
                               'Занятость: Test_2\n')


def test_vacancy_dict(vacancy_2):
    """Тестирует метод __dict__ - представление экземпляра вакансии в виде словаря"""
    assert vacancy_2.__dict__() == {
        "id": "2",
        "name": "Test_2",
        "area": "Test_2",
        "url": "Test_2",
        "salary": 50000,
        "employer": "Test_2",
        "requirement": "Test_2",
        "responsibility": "Test_2",
        "experience": "Test_2",
        "employment": "Test_2"
    }


def test_vacancy_gt(vacancy_1, vacancy_2):
    """Тестирует сравнение зарплат двух экземпляров класса Vacancy"""
    assert (vacancy_1 > vacancy_2) is False


def test_vacancy_gt_with_int(vacancy_2):
    """Тестирует сравнение зарплаты экземпляра класса Vacancy с числом"""
    assert (vacancy_2 > 30000) is True


def test_vacancy_getter_salary(vacancy_2):
    """Тестирует геттер для зарплаты"""
    assert vacancy_2.salary == 50000


def test_vacancy_setter_salary(vacancy_2):
    """Тестирует геттер для зарплаты"""
    vacancy_2.salary = 20000
    assert vacancy_2.salary == 20000


def test_vacancy_setter_salary_error(vacancy_2):
    """Тестирует геттер для зарплаты с ошибкой"""
    with pytest.raises(ValueError):
        vacancy_2.salary = -20000


def test_vacancy_cast_to_object_list(hh_vacancy_1, hh_vacancy_2):
    """Тестирует метод для преобразования списка вакансий из API сервиса с вакансиями в список экземпляров класса"""
    hh_vacancies = [hh_vacancy_1, hh_vacancy_2]
    assert len(Vacancy.cast_to_object_list(hh_vacancies)) == 2
    assert Vacancy.cast_to_object_list(hh_vacancies)[0].id == '98829845'
    assert Vacancy.cast_to_object_list(hh_vacancies)[1].id == '98973440'
    assert Vacancy.cast_to_object_list(hh_vacancies)[0].salary == 0
    assert Vacancy.cast_to_object_list(hh_vacancies)[1].salary == 0


def test_vacancy_get_salary_without_tax_gross_true(vacancy_4):
    """Тестирует метод для пересчета зарплаты без учета НДФЛ, если зарплата указана с учетом налога"""
    assert vacancy_4.get_salary_without_tax() == 1321


def test_vacancy_get_salary_without_tax_gross_false(vacancy_3):
    """Тестирует метод для пересчета зарплаты без учета НДФЛ, если зарплата указана без учета налога"""
    assert vacancy_3.get_salary_without_tax() == 180000


def test_vacancy_convert_to_rubles_byr(vacancy_4):
    """Тестирует метод для конвертации зарплаты из белорусских рублей в рубли"""
    assert vacancy_4.convert_to_rubles() == 32357


def test_vacancy_convert_to_rubles_rur(vacancy_3):
    """Тестирует метод для конвертации зарплаты из рублей в рубли"""
    assert vacancy_3.convert_to_rubles() == 180000


def test_vacancy_convert_to_rubles_usd(vacancy_5):
    """Тестирует метод для конвертации зарплаты из долларов в рубли"""
    assert vacancy_5.convert_to_rubles() == 90880
