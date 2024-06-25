from src.hh_api import HeadHunterAPI


class Vacancy:
    """
    Класс Vacancy для получения вакансий, сформированных в удобном виде на основе полученных данных API
    """
    pk: str  # Идентификатор вакансии
    name: str  # Наименование вакансии
    area: str  # Местоположение работы
    salary: dict  # Зарплата
    url: str  # Адрес страницы вакансии
    requirement: str  # Требования
    responsibility: str  # Зона ответственности

    __slots__ = ['__pk', 'name', 'area', '__salary', '__currency', '__url', 'requirement', 'responsibility']

    def __init__(self, pk, name, area, salary, url, requirement, responsibility) -> None:
        self.__pk = pk
        self.name = name
        self.area = area
        self.__salary = self.__validate_salary(salary)
        self.__currency = self.__validate_currency(salary)
        self.__url = url
        self.requirement = requirement
        self.responsibility = responsibility

    @staticmethod
    def __validate_salary(salary):
        """
        Проверяет, указана ли зарплата в вакансии
        :param salary: словарь с данными по з/п
        :return: минимальный уровень предлагаемой з/п или сообщает об отсутствии такой информации
        """
        if not salary:
            return 0
        elif not salary.get('from'):
            return salary.get('to')
        else:
            return salary.get('from')

    @staticmethod
    def __validate_currency(salary):
        """
        Функция возвращает валюту, в которой предлагают зарплату
        """
        if not salary:
            return "-"
        else:
            return salary.get('currency')

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __gt__(self, other):
        return self.__salary > other.__salary

    @classmethod
    def new_vacancy(cls, pk, name, area, salary, url, requirement, responsibility):
        """
        Метод создания класса
        :return: объект класса
        """
        return cls(pk, name, area, salary, url, requirement, responsibility)

    @property
    def pk(self):
        return self.__pk

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def currency(self):
        return self.__currency

    def __repr__(self):
        return (f'\n{self.__class__.__name__}, pk: {self.__pk}, name: {self.name},\n area: {self.area}, '
                f'salary: {self.__salary}, currency: {self.__currency}, \n'
                f'URL: {self.__url},\n requirements: {self.requirement},\n responsibility: {self.responsibility}\n')

    def __str__(self):
        return (f'id: {self.__pk}\n'
                f'Название вакансии: {self.name}\n'
                f'Город: {self.area}\n'
                f'Зарплата: {self.__salary} {self.__currency}\n'
                f'Ссылка на вакансию: {self.__url}\n'
                f'Требования к соискателю: {self.requirement}\n'
                f'Основные обязанности: {self.responsibility}\n')
