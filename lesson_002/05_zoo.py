#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
#  здесь ваш код
zoo.insert(1,'bear')
print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo = zoo+birds
print(zoo)

# уберите слона
#  и выведите список на консоль
del zoo [3]
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
for i in zoo:
    if i == 'lion':
        print(f'leon is: {zoo.index(i)}')
    if i == 'lark' :
        print(f'lark is: {zoo.index(i)}')



