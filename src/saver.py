from abc import ABC, abstractmethod

import json

from src.vacancy import Vacancy


class SaverToFile(ABC):
    @abstractmethod
    def write_data(self, data):
        raise NotImplemented()

    @abstractmethod
    def load_data(self):
        raise NotImplemented()

    @abstractmethod
    def delete_data(self, *args, **kwargs):
        raise NotImplemented()


class JSONSaver(SaverToFile):

    def __init__(self, path):
        self.__path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    def load_data(self):
        """
        Метод для открытия и распаковки файла JSON
        :return: распакованный JSON
        """
        with open(self.__path, encoding='utf-8') as file:
            return json.load(file)

    def write_data(self, vacancies: list[Vacancy]) -> None:
        """
        Метод записи вакансий в JSON-файл с добавлением данных
        """
        data_for_write = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.__path, "w", encoding='utf-8') as file:
            json.dump(data_for_write, file, ensure_ascii=False, indent=4)

    def delete_data(self):
        pass
