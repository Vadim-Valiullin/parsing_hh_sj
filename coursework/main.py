import json
import requests
from clasess import HH, Superjob, Vacancy


data_base = []
for i in range(1):             # цикл, который скачивает вакансии
    url = 'https://api.hh.ru/vacancies'
    par = {'text': 'python', 'area': '113', 'per_page': '10', 'page': i}  # параметры, которые будут добавлены к запросу
    resp = requests.get(url, params=par).json()
    data_base.append(resp)

dictionary = []
currency = None
for d in data_base:
    dict = d['items']
    #цикл, переберает объекты, т.е перебирает вакансии
    for i in dict:
        # проверяем есть ли в вакансии данные по зарплате
        if i['salary']['from'] != None:
            salary = i['salary']['from']
            if i['salary']['from'] < 10000:
                currency = 'долларов'
            else:
                currency = 'рублей'
        else:
            salary = None
        name = i['name']
        url = i['alternate_url']
        description = i['snippet']['requirement']
        dictionary.append(Vacancy(name, url, salary, currency, description))
print(dictionary[0:5])


# def main():
#     store = Store({}, 100)
#     shop = Shop({}, 20)
#     orders = []
#     fromm = "склад"
#     to = "магазин"
while True:
    print(
        'Выбрать запрос:\n1. Вывести 10 вакансии с наименьшими требованиями\n2. Вывести 5 ваканский с '
        'наибольшей зарплатой в рублях\n3.Вывести все ссылки на вакансии\n4. Вывести вакансии с зарплатой в долларах ')
    user_input = input('Ввод: ')
    if user_input.isdigit():
        if int(user_input) == 2:
            list_salaries = []
            for i in dict:
                if i['salary']['from'] != None:
                    list_salaries.append(i['salary']['from'])
                    sorted_list = sorted(list_salaries)
        print(sorted_list[-5:])


        #     product = input('Какой продукт доставить: ')
        #     amount = input(f'Сколько {product} доставить: ')
        #     orders.append(Request(fromm, to, int(amount), product))
        # elif int(user_input) == 2:
        #     for order in orders:
        #         print(f'{order}')
        # elif int(user_input) == 3:
        #     orders.clear()
        # elif int(user_input) == 4:
        #     request(orders, shop, store)
        #     orders.clear()
        # else:
        #     print('Неправильный ввод')
        #     break
