from abc import ABC, abstractmethod

import json

from src.config import VACANCIES
from src.hh_api import HeadHunterAPI
from src.utils import create_vacancies_list, filter_by_salary, filter_by_area, sort_vacancy_by_salary
from src.vacancy import Vacancy


class SaverToFile(ABC):
    @abstractmethod
    def write_data(self, data):
        raise NotImplemented()

    @abstractmethod
    def load_data(self):
        raise NotImplemented()

    @abstractmethod
    def delete_data(self, query):
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
        try:
            old_data = self.load_data()
            old_vacancies_list = create_vacancies_list(old_data)
            old_vac_ids = [old_vacancy.pk for old_vacancy in old_vacancies_list]
            data_for_write = [vacancy.to_dict() for vacancy in vacancies if vacancy.pk not in old_vac_ids]
            data_for_write.extend(old_data)
            self.__save_data(data_for_write)
        except FileNotFoundError:
            print('Файл не существует, создан новый файл')
            data_for_write = [vacancy.to_dict() for vacancy in vacancies]
            self.__save_data(data_for_write)

    # def delete_data_by_salary(self, query: dict):
    #     try:
    #         old_data = self.load_data()
    #         old_vacancies_list = create_vacancies_list(old_data)
    #         filtered_vac_list = filter_by_salary(old_vacancies_list, salary_from=query['salary_from'],
    #                                              salary_to=query['salary_to'])
    #         data_for_write = [vacancy.to_dict() for vacancy in filtered_vac_list]
    #         self.__save_data(data_for_write)
    #     except FileNotFoundError:
    #         print('Файл не существует')
    #
    # def delete_data_by_area(self, area: str):
    #     try:
    #         old_data = self.load_data()
    #         old_vacancies_list = create_vacancies_list(old_data)
    #         filtered_vac_list = filter_by_area(old_vacancies_list, area)
    #         data_for_write = [vacancy.to_dict() for vacancy in filtered_vac_list]
    #         self.__save_data(data_for_write)
    #     except FileNotFoundError:
    #         print('Файл не существует')

    def delete_data(self, query):
        pass

    def __save_data(self, data):
        with open(self.__path, "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    hh_api = HeadHunterAPI()
    hh_api.text = 'Python'
    hh_vacancies = hh_api.get_vacancies()
    vac_list: list[Vacancy] = sort_vacancy_by_salary(create_vacancies_list(hh_vacancies))
    json_obj: JSONSaver = JSONSaver(VACANCIES)
    json_obj.write_data(vac_list)

# print((vac_list))
