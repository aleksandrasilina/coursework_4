import requests


def test_head_hunter_api_init(hh_api):
    """Тестирует конструктор для API HeadHunter"""
    assert hh_api.url == 'https://api.hh.ru/vacancies'
    assert hh_api.headers == {'User-Agent': 'HH-User-Agent'}
    assert hh_api.params == {'text': '', 'page': 0, 'per_page': 100}
    assert hh_api.vacancies == []
    assert hh_api.file_worker == 'vacancies'


def test_head_hunter_api_load_vacancies(hh_api):
    """Тестирует метод для загрузки списка вакансий с API HeadHunter"""
    hh_api.load_vacancies("python")
    assert len(hh_api.vacancies) > 0


# def test_head_hunter_api_load_vacancies_response(hh_api):
#     """Тестирует метод для загрузки списка вакансий с API HeadHunter"""
#     hh_api.load_vacancies("пекарь")
#     assert requests.get(hh_api.url, headers=hh_api.headers, params=hh_api.params) == '<Response [200]>'
