from test import Store, Shop, Request


def main():
    store = Store({})
    shop = Shop({})
    fromm = "склад"
    to = "магазин"
    while True:
        print(
            'Выбрать запрос:\n1. Доставить на склад\n2. Доставить из склада в магазин\n3. Просмотреть наличие '
            'товаров в магазине и на складе')
        user_input = input('Ввод: ')
        if user_input.isdigit():
            if int(user_input) == 1:
                prod = input('Какой продукт доставить: ')
                quant = input(f'Сколько {prod} доставить: ')
                if store.add(prod, int(quant)):
                    print('Товар доставлен на склад')
                else:
                    print('Склад переполнен\nМаксимум 100 единиц товара')
            elif int(user_input) == 2:
                print(f'Выберите, что поставить в магазин из склада\nНа складе хранится: {store.get_items()}')
                prod = input('Какой продукт доставить: ')
                quant = input(f'Сколько {prod} доставить: ')
                if prod in store.get_items() and int(quant) <= store.items[prod] and shop.add(prod, int(quant)):
                    store.remove(prod, int(quant))
                    print(Request(fromm, to, int(quant), prod))
                else:
                    print('Ошибочный запрос\nПроверьте возможно таких товаров нет на складе или превышена вместимость '
                          'магазина')
            elif int(user_input) == 3:
                print(f'На складе храниться {store.get_items()}')
                print(f'В магазине продается {shop.get_items()}')


if __name__ == '__main__':
    main()
