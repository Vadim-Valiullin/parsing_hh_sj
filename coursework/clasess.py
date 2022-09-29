from abc import ABC, abstractmethod


class Engine(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def get_request(self):
        pass



class Superjob(Engine):
    def get_request(self):
        pass


class Vacancy:
    def __init__(self, name: str, url: str, salary: int, currency: str, description: str):
        self.name = name
        self.url = url
        self.salary = salary
        self.currency = currency
        self.description = description

    def __repr__(self):
        return  (f'Название вакансии: {self.name}\nСсылка на вакансию: {self.url}\nЗаработная плат'
                 f'а: {self.salary} {self.currency}\nОписание вакансии: {self.description}')
