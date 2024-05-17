import os.path
import json


def test_json_saver_init(json_saver):
    """Тестирует конструктор для сохранения вакансий в файл"""
    assert json_saver.file_name == 'test_vacancies.json'


def test_json_saver_add_vacancies(vacancy_1, vacancy_2, vacancy_3, json_saver):
    """Тестирует метод для сохранения списка экземпляров вакансий в файл"""
    vacancies_list = [vacancy_1, vacancy_2, vacancy_3]
    json_saver.add_vacancies(vacancies_list)
    with open(os.path.join('C:/Users/Александра/PycharmProjects/coursework_4/data', json_saver.file_name), 'r',
              encoding='utf-8') as file:
        assert len(json.load(file)) == 3


def test_json_saver_get_vacancies(vacancy_1, vacancy_2, vacancy_3, json_saver):
    """Тестирует метод для возвращения содержимого файла"""
    vacancies_list = [vacancy_1, vacancy_2, vacancy_3]
    json_saver.add_vacancies(vacancies_list)  # добавляем список вакансий в файл
    assert len(json_saver.get_vacancies()) == 3


def test_json_saver_filter_vacancies(vacancy_1, vacancy_2, vacancy_3, json_saver):
    """Тестирует метод для метод для получения вакансий из файла по указанным критериям"""
    vacancies_list = [vacancy_1, vacancy_2, vacancy_3]
    json_saver.add_vacancies(vacancies_list)  # добавляем список вакансий в файл
    keywords = ['test_1', '1']
    assert len(json_saver.filter_vacancies(keywords)) == 1
    assert json_saver.filter_vacancies(keywords)[0].id == '1'
    assert json_saver.filter_vacancies(keywords)[0].name == 'Test_1'


def test_json_saver_add_vacancy(vacancy_1, vacancy_2, vacancy_3, json_saver):
    """Тестирует метод для метод для добавления вакансии в файл"""
    vacancies_list = [vacancy_1, vacancy_2]
    json_saver.add_vacancies(vacancies_list)  # добавляем список вакансий в файл
    json_saver.add_vacancy(vacancy_3)  # добавляем одну вакансию в файл
    assert len(json_saver.get_vacancies()) == 3
    assert json_saver.get_vacancies()[2]['id'] == '3'
    assert json_saver.get_vacancies()[2]['name'] == 'Test_3'


def test_json_saver_delete_vacancy(vacancy_1, vacancy_2, vacancy_3, json_saver):
    """Тестирует метод для метод для удаления вакансии из файла"""
    vacancies_list = [vacancy_1, vacancy_2, vacancy_3]
    json_saver.add_vacancies(vacancies_list)  # добавляем список вакансий в файл
    json_saver.delete_vacancy(vacancy_3)  # удаляем одну вакансию из файла
    assert len(json_saver.get_vacancies()) == 2
