import pytest

from src.exceptions import HeadHunterAPIException


def test_get_vacancies_without_text(hh_api):
    """
    Тест для проверки получения ошибки без ввода параметра поиска вакансии.
    """
    with pytest.raises(HeadHunterAPIException):
        hh_api.get_vacancies()


def test_get_vacancies(hh_api):
    """
    Тест проверки получения списка вакансий при введенном параметре
    ВАЖНО! Перед запуском теста необходимо в файле hh_api.py получить обновленный список вакансий и ввести id
    из первой вакансии.
    """
    hh_api.text = 'Python'
    hh_api.params['per_page'] = 1
    assert hh_api.get_vacancies()[0].get('id') == '102264189'


def test_text(hh_api):
    """
    Тестирование геттера
    """
    assert hh_api.text is None


def test_text_setter(hh_api):
    """
    Тестирование сеттера
    """
    hh_api.text = 'python'
    assert hh_api.text == 'python'


def test_connect_to_api_without_text(hh_api):
    """
    Тест для проверки получения ошибки подключения к API без ввода параметра поиска вакансии.
    """
    with pytest.raises(HeadHunterAPIException):
        hh_api.connect_to_api()


def test_connect_to_api(hh_api):
    """
    Тест проверки подключения к API.
    """
    hh_api.text = 'Python'
    resp = hh_api.connect_to_api()
    assert hh_api._check_status(resp) is True
