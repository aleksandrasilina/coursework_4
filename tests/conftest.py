import pytest

from src.currency_converter_erapi import CurrencyConverterERAPI
from src.head_hunter_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1():
    return Vacancy('1', 'Test_1', 'Test_1',
                   'Test_1',
                   'Test_1',
                   'Test_1',
                   'Test_1',
                   'Test_1',
                   'Test_1'
                   )


@pytest.fixture
def vacancy_2():
    return Vacancy('2', 'Test_2', 'Test_2',
                   'Test_2',
                   'Test_2',
                   'Test_2',
                   'Test_2',
                   'Test_2',
                   'Test_2',
                   50000
                   )


@pytest.fixture
def vacancy_3():
    return Vacancy('3', 'Test_3', 'Test_3',
                   'Test_3',
                   'Test_3',
                   'Test_3',
                   'Test_3',
                   'Test_3',
                   'Test_3',
                   {
                       'currency': 'RUR',
                       'from': 180000,
                       'gross': False,
                       'to': None
                   }
                   )


@pytest.fixture
def vacancy_4():
    return Vacancy('4', 'Test_4', 'Test_4',
                   'Test_4',
                   'Test_4',
                   'Test_4',
                   'Test_4',
                   'Test_4',
                   'Test_4',
                   {
                       'currency': 'BYR',
                       'from': 1000,
                       'gross': True,
                       'to': None
                   }
                   )


@pytest.fixture
def vacancy_5():
    return Vacancy('5', 'Test_5', 'Test_5',
                   'Test_5',
                   'Test_5',
                   'Test_5',
                   'Test_5',
                   'Test_5',
                   'Test_5',
                   {
                       'currency': 'USD',
                       'from': 1000,
                       'gross': False,
                       'to': None
                   }
                   )


@pytest.fixture
def vacancy_6():
    return Vacancy('6', 'Test_6', 'Test_6',
                   'Test_6',
                   'Test_6',
                   'Test_6',
                   'Test_6',
                   'Test_6',
                   'Test_6',
                   {
                       'currency': 'RUR',
                       'from': None,
                       'gross': False,
                       'to': 100000
                   }
                   )


@pytest.fixture
def hh_vacancy_1():
    return {'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': None,
            'adv_context': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/98829845',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=98829845',
            'archived': False,
            'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
            'contacts': None,
            'created_at': '2024-05-13T17:47:04+0300',
            'department': None,
            'employer': {'accredited_it_employer': True,
                         'alternate_url': 'https://hh.ru/employer/4080',
                         'id': '4080',
                         'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/5659385.jpeg',
                                       '90': 'https://img.hhcdn.ru/employer-logo/5659384.jpeg',
                                       'original': 'https://img.hhcdn.ru/employer-logo-original/1009652.jpg'},
                         'name': 'Axenix (ранее Accenture)',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/4080',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4080'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'has_test': False,
            'id': '98829845',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Автотестировщик(Java)',
            'premium': False,
            'professional_roles': [{'id': '124', 'name': 'Тестировщик'}],
            'published_at': '2024-05-13T17:47:04+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': None,
            'schedule': {'id': 'remote', 'name': 'Удаленная работа'},
            'show_logo_in_search': None,
            'snippet': {'requirement': 'Test',
                        'responsibility': 'Test'},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/98829845?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []}


@pytest.fixture
def hh_vacancy_2():
    return {'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': None,
            'adv_context': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/98973440',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=98973440',
            'archived': False,
            'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
            'branding': {'tariff': None, 'type': 'MAKEUP'},
            'contacts': None,
            'created_at': '2024-05-14T22:25:21+0300',
            'department': None,
            'employer': {'accredited_it_employer': False,
                         'alternate_url': 'https://hh.ru/employer/49357',
                         'id': '49357',
                         'logo_urls': {'240': 'https://img.hhcdn.ru/ichameleon/310823.png',
                                       '90': 'https://img.hhcdn.ru/ichameleon/310823.png',
                                       'original': 'https://img.hhcdn.ru/ichameleon/310823.png'},
                         'name': 'МАГНИТ, Розничная сеть',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/49357',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=49357'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'has_test': False,
            'id': '98973440',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Middle C++ разработчик',
            'premium': False,
            'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
            'published_at': '2024-05-14T22:25:21+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': None,
            'schedule': {'id': 'remote', 'name': 'Удаленная работа'},
            'show_logo_in_search': True,
            'snippet': {'requirement': 'Test',
                        'responsibility': 'Test'},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/98973440?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []}


@pytest.fixture
def hh_api():
    return HeadHunterAPI('vacancies')


@pytest.fixture
def cc_api():
    return CurrencyConverterERAPI('CNY', 1000)


@pytest.fixture
def json_saver():
    return JSONSaver(HeadHunterAPI('test_vacancies'))


@pytest.fixture
def user():
    return {'search_query': 'python',
            'keywords': ['junior', 'Москва'],
            'top_n': 20,
            'salary_from': 50000,
            'file_worker': 'vacs'}
