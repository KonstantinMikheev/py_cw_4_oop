from src.vacancy import Vacancy


def test_new_vacancy():
    vacancy = Vacancy.new_vacancy(pk='102136724',
                                  name='Middle Python Developer',
                                  area="Москва",
                                  salary=None,
                                  requirement='Опыт коммерческой разработки на Python от 3х лет',
                                  responsibility='Разработка ERP системы группы компаний',
                                  url='https://hh.ru/vacancy/102300750')
    assert isinstance(vacancy, Vacancy) is True


def test___validate_salary(vacancy1, vacancy2, vacancy3):
    assert vacancy1.salary == 0
    assert vacancy2.salary == 350000
    assert vacancy3.salary == 450000


def test___validate_currency(vacancy1, vacancy2):
    assert vacancy1.currency == "-"
    assert vacancy2.currency == "RUR"
