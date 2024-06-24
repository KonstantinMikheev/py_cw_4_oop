from json import JSONDecodeError

import requests

from abc import ABC, abstractmethod

from src.exceptions import HeadHunterAPIException


class API(ABC):
    """
    Абстрактный класс для подключения и получения данных с API-ресурсами
    """

    @abstractmethod
    def connect_to_api(self):
        """
        Абстрактный метод подключения к API
        """
        raise NotImplemented()

    @abstractmethod
    def get_vacancies(self):
        """
        Абстрактный метод получения вакансий
        """
        raise NotImplemented()

    @staticmethod
    @abstractmethod
    def _check_status(response) -> bool:
        """
        Абстрактный метод проверки статуса подключения к API
        """
        raise NotImplemented()


class HeadHunterAPI(API):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url: str = 'https://api.hh.ru/vacancies'
        self.headers: dict = {'User-Agent': 'HH-User-Agent'}
        self.__text = None
        self.params: dict = {
            'page': 0,
            'per_page': 100,
            'search_field': 'name'}
        self.vacancies: list = []

    @property
    def text(self) -> str:
        """
        Метод получения текста, являющегося параметром для поиска вакансий.
        По умолчанию None
        """
        return self.__text

    @text.setter
    def text(self, text) -> None:
        """
        Сеттер для защищенного параметра text
        """
        self.__text = text

    def connect_to_api(self):
        """
        Метод для подключения к API HH.RU по указанным параметрам
        :return: объект класса Response
        """
        if self.__text is None:
            raise HeadHunterAPIException("Поисковый запрос не задан")
        else:
            self.params['text'] = self.__text
            return requests.get(self.__url, headers=self.headers, params=self.params)

    def get_vacancies(self) -> list:
        """
        Метод для получения JSON-файла с вакансиями, полученными по заданному параметру
        :return: JSON
        """
        while self.params.get('page') != 20:
            response = self.connect_to_api()
            is_allowed = self._check_status(response)
            if not is_allowed:
                raise HeadHunterAPIException(f'''Ошибка запроса данных. Статус запроса: {response.status_code}, 
                response: {response.text}''')
            try:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
            except JSONDecodeError:
                raise HeadHunterAPIException(f'Ошибка данных. Получен не JSON-объект. Получен {response}')

        return self.vacancies

    @staticmethod
    def _check_status(response) -> bool:
        """
        Метод проверки успешного подключения к API HH.RU
        :param response: объект класса Response
        :return: bool
        """
        return response.status_code == 200


# if __name__ == '__main__':
#
#     hh_api = HeadHunterAPI()
#     hh_api.text = 'Python'
#     hh_api.params['per_page'] = 1
#     hh_vacancies = hh_api.get_vacancies()
#     resp = hh_api.connect_to_api()
#     print(resp)
#     print(hh_api._check_status(resp))
#     print(hh_vacancies)
