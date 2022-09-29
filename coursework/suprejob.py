import requests
from bs4 import BeautifulSoup
from clasess import HH, Superjob, Vacancy


HOST = 'https://russia.superjob.ru/'
URL = 'https://russia.superjob.ru/vacancy/search/?keywords=python'
HEADERS = {
    'Accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent':	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
}


def get_data(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('span', class_='f-test-search-result-item')
    dictionary = []

    for item in items:
        dictionary.append(
            {
                'name': item.find('span', class_="_9fIP1 _249GZ _1jb_5 QLdOc").get_text(),
                'url': HOST + item.find('span', class_="_9fIP1 _249GZ _1jb_5 QLdOc").find('a').get('href'),
                'salary': item.find('span', class_="_2eYAG _1nqY_ _249GZ _1dIgi").get_text(),
                'description': item.find('span', class_="_39I1Z _1Nj4W _249GZ _1jb_5 _1dIgi _3qTky").get_text()

            }
        )
        return dictionary


def load_content(items):
    with open('superjob.txt', 'w', newline='') as file:
        for item in items:
            writer = file.write(Vacancy('name', 'url', 'salary', 'description'))

def parser():
    PAGENATION = input('Указать количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_data(URL)
    if html.status_code == 200:
        sj_dict = []
        for page in range(1, PAGENATION):
            print(f'Парсим страницу: {page}')
            html = get_data(URL, params={'page': page})
            sj_dict.extend(get_content(html.text))
            load_content(sj_dict)
        print('Парсинг закончился')
        print(dictionary)
        pass
    else:
        print('Error')


parser()



















# def make_superjob_request(relative_url, url_params=None):
#
#     response = requests.get('https://api.superjob.ru/2.0/%s' % relative_url,
#                             params=url_params, headers=headers)
#     return response.json()
#
#
# def get_moscow_programmers():
#     catalogue_id = 48 # id каталога "Разработка, программирование"
#     town_id = 4 # id города Москва
#     vacancies_count = 100 # api запрещает запрашивать больше 100 вакансий
#     keyword = 'Программист'
#     params={'town': town_id, 'catalogues': catalogue_id, 'count': vacancies_count, 'keyword': keyword}
#     return make_superjob_request('vacancies/', params)
#
# if __name__ == '__main__':
#     response = get_moscow_programmers()
#     vacancies = response['objects']
#     # out_filename = sys.argv[1] if len(sys.argv) == 2 else 'full_vacancies.json'
#     # db_helpers.save_object_to_file(vacancies, out_filename)
#     print("Done")
#
# import json
#
#
# def save_object_to_file(object_to_save, output_filename):
#     with open(output_filename, 'w') as outfile:
#         json.dump(object_to_save, outfile)
#
#
# def get_object_from_file(input_filename):
#     with open(input_filename, 'r') as infile:
#         return json.load(infile)
#
# def get_vacancy_description_and_payment(vacancy):
#     result = {}
#     result['profession'] = vacancy['profession'] or ''
#     result['candidat'] = vacancy['candidat'] or ''
#     result['payment_from'] = vacancy['payment_from'] or 0
#     result['payment_to'] = vacancy['payment_to'] or 0
#     return result
#
# "payment_from": 0,
#         "payment_to": 0,
# "profession": "Специалист по согласованиям",
#         "work": "1. Подготовка, согласование с Комитетами и службами...",
# "currency": "rub",
# "link": "https://www.superjob.ru/clients/vladhleb-745208.html",