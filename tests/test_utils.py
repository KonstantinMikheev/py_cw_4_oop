import pytest

from src.utils import sort_vacancy_by_salary, create_vacancies_list
from src.vacancy import Vacancy


def test_sort_vacancy_by_salary(vacancies_list):
    sorted_list = sort_vacancy_by_salary(vacancies_list)
    assert [i.salary for i in sorted_list] == [450000, 350000, 0]


def test_create_vacancies_list(vacancies_list_for_create):
    sorted_list:list[Vacancy] = create_vacancies_list(vacancies_list_for_create)
    assert [450000, 350000, 0] == [i.salary for i in sorted_list]
