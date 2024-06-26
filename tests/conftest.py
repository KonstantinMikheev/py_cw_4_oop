import pytest

from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


@pytest.fixture
def hh_api_with_request():
    hh_api_request = HeadHunterAPI()
    hh_api_request.text = 'Python'
    hh_api_request.params['per_page'] = 1
    return hh_api_request.get_vacancies()[0].get('id')


@pytest.fixture
def vacancy1():
    return Vacancy(pk='102136724', name='Middle Python Developer', area="Москва",
                   salary=None,
                   requirement='Опыт коммерческой разработки на Python от 3х лет',
                   responsibility='Разработка ERP системы группы компаний', url='https://hh.ru/vacancy/102300750')


@pytest.fixture
def vacancy2():
    return Vacancy(pk='102136724', name='Middle Python Developer', area="Уфа",
                   salary={"from": 350000, "to": None, "currency": "RUR"},
                   requirement='Опыт коммерческой разработки на Python от 3х лет',
                   responsibility='Разработка ERP системы группы компаний', url='https://hh.ru/vacancy/102300750')


@pytest.fixture
def vacancy3():
    return Vacancy(pk='102136724', name='Middle Python Developer', area="Казань",
                   salary={"from": None, "to": 450000, "currency": "RUR"},
                   requirement='Опыт коммерческой разработки на Python от 3х лет',
                   responsibility='Разработка ERP системы группы компаний', url='https://hh.ru/vacancy/102300750')


@pytest.fixture
def vacancies_list(vacancy1, vacancy2, vacancy3):
    return [vacancy1, vacancy2, vacancy3]


@pytest.fixture
def vacancies_list_for_create():
    return [{'id': '102136724', 'name': 'Middle Python Developer', 'area': {"name": "Москва"},
             'salary': None,
             'snippet': {'requirement': 'Опыт коммерческой разработки на Python от 3х лет',
                         'responsibility': 'Разработка ERP системы группы компаний'},
             'alternate_url': 'https://hh.ru/vacancy/102300750'},
            {'id': '102136724', 'name': 'Middle Python Developer', 'area': {"name": "Москва"},
             'salary': {"from": 350000, "to": None, "currency": "RUR"},
             'snippet': {'requirement': 'Опыт коммерческой разработки на Python от 3х лет',
                         'responsibility': 'Разработка ERP системы группы компаний'},
             'alternate_url': 'https://hh.ru/vacancy/102300750'},
            {'id': '102136724', 'name': 'Middle Python Developer', 'area': {"name": "Москва"},
             'salary': {"from": None, "to": 450000, "currency": "RUR"},
             'snippet': {'requirement': 'Опыт коммерческой разработки на Python от 3х лет',
                         'responsibility': 'Разработка ERP системы группы компаний'},
             'alternate_url': 'https://hh.ru/vacancy/102300750'}]

