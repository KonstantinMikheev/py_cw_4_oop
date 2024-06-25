from src.vacancy import Vacancy
from src.hh_api import HeadHunterAPI


def create_vacancies_list(vacancy_data):
    """
    Функция для получения списка вакансий в заданном формате при помощи класса Vacancy на основании полученных данных.
    :param vacancy_data список словарей
    :return: список объектов класса Vacancy
    """
    return [Vacancy.new_vacancy(vacancy) for vacancy in vacancy_data]


def sort_vacancy_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Функция сортировки вакансий по зарплате. Реверс тру настроен на сортировку от большего к меньшему.
    """
    return sorted(vacancies, reverse=True)


def filter_by_salary(salary_from: int, salary_to: int, vacancies: list[Vacancy]):
    filtered_vacancies = []
    for vacancy in vacancies:
        if salary_from <= vacancy.salary <= salary_to:
            filtered_vacancies.append(vacancy)
    return filtered_vacancies


def filter_by_area(vacancies: list[Vacancy], area: str):
    vacancies_in_area = []
    for vac in vacancies:
        if area.strip().lower() == vac.area.strip().lower():
            vacancies_in_area.append(vac)
    return vacancies_in_area


def filter_by_keyword(vacancies: list[Vacancy], keyword: str):
    vacancies = [vac.to_dict() for vac in vacancies]
    vacancies_with_keyword = []
    for vac in vacancies:
        vac_values = []
        for v in vac.values():
            if keyword in str(v).strip().lower():
                vac_values.append(v)
        if len(vac_values) > 0:
            vacancies_with_keyword.append(vac)
    return vacancies_with_keyword


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Возвращает топ N по зарплате
    """
    return sorted_vacancies[:top_n]


if __name__ == '__main__':
    hh_api = HeadHunterAPI()
    hh_api.text = 'Python'
    hh_vacancies = hh_api.get_vacancies()
    vac_list = create_vacancies_list(hh_vacancies)
    print(filter_by_keyword(vac_list, "опыт работы"))
