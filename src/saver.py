from abc import ABC, abstractmethod

import json
from json import JSONDecodeError
from pathlib import Path

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

    def __init__(self, filename):
        self.__filename = f'{filename}.json'

    @property
    def filename(self):
        return self.__filename

    def path(self):
        return Path(__file__).parent.parent.joinpath("data", self.filename)

    def load_data(self):
        """
        Метод для открытия и распаковки файла JSON
        :return: распакованный JSON
        """
        with open(self.path(), encoding='utf-8') as file:
            return json.load(file)

    def write_data(self, vacancies: list[Vacancy]) -> None:
        """
        Метод записи вакансий в JSON-файл с добавлением данных
        """
        new_data = [vacancy.to_dict() for vacancy in vacancies]
        old_data = self.load_data()
        if old_data:
            old_data.extend(new_data)
            with open(self.path(), "a", encoding='utf-8') as file:
                json.dump(old_data, file, ensure_ascii=False, indent=4)

        else:
            with open(self.path(), "w", encoding='utf-8') as file:
                json.dump(new_data, file, ensure_ascii=False, indent=4)

    def delete_data(self):
        """
        Метод очищает JSON-файл от содержимого.
        """
        try:
            data_to_delete = None
            with open(self.path(), "w", encoding='utf-8') as file:
                json.dump(data_to_delete, file, ensure_ascii=False, indent=4)
        except JSONDecodeError:
            return
