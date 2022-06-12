# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
all_goods = goods.keys()
for i in all_goods:

    if i == 'Лампа':
        lamp = i
    if i == 'Стол':
        table = i
    if i == 'Диван':
        sofa = i
    if i == 'Стул':
        chair = i

lamps = store[goods['Лампа']]
tables = store[goods['Стол']]
sofas = store[goods['Диван']]
chairs = store[goods['Стул']]


# print(lamp)
def shope(good, goodes):
    z = 0
    z1 = 0
    for i in goodes:
        for j in i:
            if j == 'quantity':
                z += i[j]
            if j == 'price':
                z1 += i[j]
    print(f'quantity {good} is {z}')
    print(f'price {good} is {z1}')
    print()

aa1 = shope(good=lamp, goodes=lamps)
aa2 = shope(good=table, goodes=tables)
aa3 = shope(good=sofa, goodes=sofas)
aa4 = shope(good=chair, goodes=chairs)
# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе
