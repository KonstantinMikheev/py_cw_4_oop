from src.vacancy import Vacancy


def test_new_vacancy():
    data = {'id': '102136724', 'name': 'Middle Python Developer', 'area': {"name": "Москва"},
             'salary': None,
             'snippet': {'requirement': 'Опыт коммерческой разработки на Python от 3х лет',
                         'responsibility': 'Разработка ERP системы группы компаний'},
             'alternate_url': 'https://hh.ru/vacancy/102300750'}
    vacancy = Vacancy.new_vacancy(data)
    assert isinstance(vacancy, Vacancy) is True


def test___validate_salary(vacancy1, vacancy2, vacancy3):
    assert vacancy1.salary == 0
    assert vacancy2.salary == 350000
    assert vacancy3.salary == 450000


def test___validate_currency(vacancy1, vacancy2):
    assert vacancy1.currency == "-"
    assert vacancy2.currency == "RUR"
