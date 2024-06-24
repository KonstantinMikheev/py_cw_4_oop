import pytest

from src.hh_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    return HeadHunterAPI()

@pytest.fixture
def hh_api_with_request():
    hh_api_request = HeadHunterAPI()
    hh_api_request.text = 'Python'
    hh_vacancies = hh_api.get_vacancies()
