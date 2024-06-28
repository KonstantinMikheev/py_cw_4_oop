from src.config import FILENAME
from src.hh_api import HeadHunterAPI
from src.saver import JSONSaver
from src.utils import create_vacancies_list, filter_by_salary, sort_vacancy_by_salary, \
    get_top_vacancies, print_vacancies, input_top_n, input_salary_range, filter_by_area


def user_interaction():
    """
    Функция взаимодействия с пользователем
    :return: список вакансий по заданным критериям поиска
    """
    search_query = input("""Добрый день! \n
    \rДля поиска вакансий на сайте hh.ru введите поисковый запрос,\n 
    \rнапример, название интересующей вас вакансии:   
    """)
    hh_api = HeadHunterAPI()
    hh_api.text = search_query
    hh_vacancies = hh_api.get_vacancies()
    vacancies_list = create_vacancies_list(hh_vacancies)
    json_saver = JSONSaver(FILENAME)
    json_saver.delete_data()
    json_saver.write_data(vacancies_list)
    filtered_city = input("Введите название города для поиска вакансии: ")
    filtered_vacancies = filter_by_area(vacancies_list, filtered_city)
    salary_range = input_salary_range()
    ranged_vacancies = filter_by_salary(salary_range, filtered_vacancies)
    sorted_vacancies = sort_vacancy_by_salary(ranged_vacancies)
    top_n = input_top_n()
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
