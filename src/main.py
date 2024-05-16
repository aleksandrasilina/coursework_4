from src import utils
from src.head_hunter_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def user_interaction():
    search_query = input("Введите поисковый запрос для поиска вакансий: ")
    keywords = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_from = int(input("Введите желаемую зарплату: "))
    file_worker = input("Введите название файла для сохранения информации о вакансиях: ")

    head_hunter_api = HeadHunterAPI(file_worker)
    head_hunter_api.load_vacancies(search_query)
    vacancies_object_list = Vacancy.cast_to_object_list(head_hunter_api.vacancies)
    json_saver = JSONSaver(head_hunter_api)
    json_saver.add_vacancies(vacancies_object_list)

    filtered_vacancies = json_saver.filter_vacancies(keywords)
    ranged_vacancies = utils.get_vacancies_by_salary(filtered_vacancies, salary_from)
    sorted_vacancies = utils.sort_vacancies(ranged_vacancies)
    top_vacancies = utils.get_top_vacancies(sorted_vacancies, top_n)
    json_saver.add_vacancies(top_vacancies)
    utils.print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
