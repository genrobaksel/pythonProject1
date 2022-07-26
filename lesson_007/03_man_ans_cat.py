# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint
from termcolor import cprint

class Men:

    def __init__(self):
        self.name = 'Victor'
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'I am {}, fullnes is {}'.format(
            self.name,self.fullness)

    def go_to_clean_shop(self):
        self.house.money-=10
        cprint(f'clean shop for {self.cat}',color='blue')
        self.house.cat_duty-=30

    def cat_food(self):
        self.cat.cat_fullness+=10
        self.house.money-=10
        print('cat was eating')


    def eat (self):

        if self.house.food > 10:
            print ('{} eaten'.format(self.name) )
            self.fullness+=10
            self.house.food-=10
        else:
            print('{} without eat'.format(self.name))

    def work (self):
        print ('{} go to job'.format(self.name))
        self.house.money+=50
        self.fullness-=10

    def watch_tv (self):
        cprint ('{} watch MTV all day'.format(self.name), color='red')
        self.fullness-=20

    def shop(self):
        self.house.cat_food+=50
        self.house.money-=10
        if self.house.money>=50:
            print('{} go to shop'.format(self.name))
            self.house.money-=10
            self.house.food+=20
        else:
            cprint('NOT Money')

    def go_into_house(self, house):
        self.house = house
        self.fullness-=10
        print(f'{self.name} - moving to the house')

    def go_to_cat(self, cat):

        self.cat = cat
        print(f'{self.name} - take the cat {self.cat.cat_name}')

    def act(self):

        if self.house.food<=0:
            self.eat()

        if self.house.money<=0:
            self.work()
        dice = randint(1, 6)
        if self.fullness<=10:
            self.shop()
            self.eat()

        elif dice ==1:
            self.work()
        elif dice ==2:
            self.eat()
        else:
            self.watch_tv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cat_food = 0
        self.cat_duty = 0
    def __str__(self):
        return 'food have {}, money is {}, cat-food have {}, cat-duty is {}'.format(
            self.food,self.money, self.cat_food, self.cat_duty)

class Cat:
    def __init__(self):
        self.cat_fullness = 50
        self.cat_name = 'marsik'
        self.house = None
        self.men = None

    def __str__(self):
        return f'Cat: {self.cat_name} have cat-food:  {self.house.cat_food}  and cat-fullness {self.cat_fullness}'

    def cat_food(self):
        self.men.work()
        self.house.cat_food-=20
        self.cat_fullness+=30

    def cat_fullness(self):
        if self.cat_fullness<= 10:
            self.men.cat_food()
        self.house.cat_food-=10

    def cat_play(self):
        self.house.cat_duty+=10

    def cat_clean(self):
        self.men.go_to_clean_shop()
        self.house.money-=10

    def cat_go_house(self, men, house):
        print('cat was the man and the house ')
        self.men= men
        self.house=house


    def cat_act(self):
        self.cat_play()
        self.cat_fullness-=10
        if self.house.cat_food <= 10:
            self.men.shop()
        if self.house.cat_duty>=50:
            self.cat_clean()
        if self.cat_fullness<=10:
            self.cat_food()



home = House()
marsik = Cat()

victor = Men()

victor.go_into_house(house=home)
victor.go_to_cat(cat=marsik)
marsik.cat_go_house( house=home,men=victor)

for day in range (1,15):
    cprint(f'============= day - {day}====================', color='green')
    victor.act()

    marsik.cat_act()
    print(victor)

    print(marsik)
    print(home)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
