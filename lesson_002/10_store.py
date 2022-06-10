#!/usr/bin/env python
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
chair = goods['Стул']
chair_code = store[chair]
chairs_quantity0 = chair_code[0]['quantity']
chairs_quantity1 = chair_code[1]['quantity']
chairs_quantity2 = chair_code[2]['quantity']
chair_price0 = chair_code[0]['price']
chair_price1 = chair_code[1]['price']
chair_price2 = chair_code[2]['price']
chairs_quantity_sum = chairs_quantity0+chairs_quantity1+chairs_quantity2
chairs_price_sum=chair_price0+chair_price2+chair_price1
all_sum_cost_chair = chairs_quantity_sum*chairs_price_sum
print('Стул -', chairs_quantity_sum, 'шт, стоимость', all_sum_cost_chair, 'руб')


a = goods['Стол']
b = store[a]
print(b)
c1 = b[0]['quantity']
c11 = b[0]['price']
c2 = b[1]['quantity']
c21 = b[1]['price']
c3 = c1+c2
c4 =c11+c21
c5 = c3*c4
print('Стол -', c3, 'шт, стоимость', c5, 'руб')


# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print(lamps_item)
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

#  здесь ваш код



##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






