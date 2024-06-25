from src.vacancy import Vacancy
from src.hh_api import HeadHunterAPI


def create_vacancies_list(vacancy_data):
    """
    Функция для получения списка вакансий в заданном формате при помощи класса Vacancy на основании полученных данных
    :param vacancy_data список словарей
    :return: список объектов класса Vacancy
    """
    vacancies_list = []
    for vacancy in vacancy_data:
        vac_ob = Vacancy(
            pk=vacancy.get('id'),
            name=vacancy.get('name'),
            url=vacancy.get('alternate_url'),
            area=vacancy.get('area').get('name'),
            salary=vacancy.get('salary'),
            requirement=vacancy.get('snippet').get('requirement'),
            responsibility=vacancy.get('snippet').get('responsibility'))
        vacancies_list.append(vac_ob)
    return sort_vacancy_by_salary(vacancies_list)


def sort_vacancy_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Функция сортировки вакансий по зарплате. Реверс тру настроен на сортировку от большего к меньшему.
    """
    return sorted(vacancies, reverse=True)


if __name__ == '__main__':
    hh_api = HeadHunterAPI()
    hh_api.text = 'Python'
    hh_api.params['per_page'] = 1
    hh_vacancies = hh_api.get_vacancies()
    vac_list = create_vacancies_list(hh_vacancies)
    print(vac_list)
