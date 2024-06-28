from src.vacancy import Vacancy
from src.hh_api import HeadHunterAPI


def create_vacancies_list(vacancy_data: list[HeadHunterAPI]) -> list[Vacancy]:
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


def filter_by_salary(salary_range: list[int], vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Функция отбора вакансий из списка вакансий по заданному уровню зарплат
    :param salary_range: значение з/п "от"-"до"
    :param vacancies: список вакансий
    :return: отфильтрованный по зарплате список вакансий
    """
    filtered_vacancies = []
    if salary_range[0] <= salary_range[1]:
        salary_from = salary_range[0]
        salary_to = salary_range[1]
    else:
        salary_from = salary_range[1]
        salary_to = salary_range[0]
    for vacancy in vacancies:
        if salary_from <= vacancy.salary <= salary_to:
            filtered_vacancies.append(vacancy)
    return filtered_vacancies


def filter_by_area(vacancies: list[Vacancy], area: str) -> list[Vacancy]:
    vacancies_in_area = []
    if not area:
        return vacancies
    else:
        for vac in vacancies:
            if area.strip().lower() == vac.area.strip().lower():
                vacancies_in_area.append(vac)
        return vacancies_in_area


def filter_by_keywords(vacancies: list[Vacancy]) -> list[dict]:
    """
    Функция отбора вакансий по введенным через запятую параметрам
    :param vacancies: список вакансий
    :param keywords: строка с параметрами отбора вакансий через запятую
    :return: список вакансий
    """
    keywords = input("Введите параметры отбора вакансий через запятую: ").split(",")
    vacancies = [vac.to_dict() for vac in vacancies]
    vacancies_with_keywords = []
    for vac in vacancies:
        vac_values = []
        for value in vac.values():
            for keyword in keywords:
                if keyword.strip().lower() in str(value).strip().lower():
                    vac_values.append(value)
        if len(vac_values) > 0:
            vacancies_with_keywords.append(vac)
    return vacancies_with_keywords


def get_top_vacancies(sorted_vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Возвращает топ N по зарплате
    """
    return sorted_vacancies[:top_n]


def print_vacancies(vacancies: list[Vacancy]) -> None:
    """
    Вывод на консоль списка вакансий (применяется Vacancy.__str__)
    """
    for vacancy in vacancies:
        print(vacancy)


def input_top_n():
    """
    Функция проверки правильности ввода пользователем топ N по уровню зарплаты
    :return: количество топ N
    """
    attempts = 0
    while attempts != 2:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N по уровню зарплаты: "))
            return top_n
        except ValueError:
            print('Введены неверные данные, попробуйте снова.\n')
            attempts += 1
            if attempts == 2:
                print("Вы не ввели корректные данные, значение принято по умолчанию и равно 10")
                return 10


def input_salary_range():
    """
     Функция проверки правильности ввода пользователем уровня зарплаты для отбора
    :return: список из значений поиска "от" и "до"
    """
    attempts = 0
    while attempts != 2:
        try:
            salary_range = input("Введите диапазон зарплат, например: 100000-150000:    ").split('-')
            return [int(salary.strip()) for salary in salary_range]
        except ValueError:
            print('Неверный диапазон, введите в формате ххх-ууу, где ххх - значение "от", ууу - значение "до"\n')
            attempts += 1
            if attempts == 2:
                print("Вы не ввели корректные данные, диапазон принят по умолчанию от 0 до 500000")
                return [0, 500000]
