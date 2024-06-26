import pytest

from src.utils import sort_vacancy_by_salary, create_vacancies_list, filter_by_salary, filter_by_area, get_top_vacancies
from src.vacancy import Vacancy


def test_sort_vacancy_by_salary(vacancies_list):
    sorted_list = sort_vacancy_by_salary(vacancies_list)
    assert [i.salary for i in sorted_list] == [450000, 350000, 0]


def test_create_vacancies_list(vacancies_list_for_create):
    vacancy_list: list[Vacancy] = create_vacancies_list(vacancies_list_for_create)
    assert [0, 350000, 450000] == [i.salary for i in vacancy_list]


def test_filter_by_salary(vacancies_list, vacancy1, vacancy2, vacancy3):
    ex1 = filter_by_salary([0, 100000], vacancies_list)
    ex2 = filter_by_salary([0, 400000], vacancies_list)
    ex3 = filter_by_salary([0, 450000], vacancies_list)
    assert ex1[0].salary == 0
    assert ex2 == [vacancy1, vacancy2]
    assert ex3 == [vacancy1, vacancy2, vacancy3]


def test_filter_by_area(vacancies_list, vacancy3):
    assert filter_by_area(vacancies_list, "Казань") == [vacancy3]


def test_filter_by_wrong_area(vacancies_list):
    assert filter_by_area(vacancies_list, "dfrg") == []


def test_get_top_vacancies(vacancies_list, vacancy1, vacancy2):
    assert get_top_vacancies(vacancies_list, 2) == [vacancy1, vacancy2]
