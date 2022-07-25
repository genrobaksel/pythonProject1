# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
class Game:

    def __init__(self):
        self.water = 'water'
        self.air = 'air'
        self.fire = 'fire'
        self.mud = 'mud'
        self.dust = 'dust'
        self.flash = 'flash'
        self.steam = 'steam'
        self.storm = 'storm'
        self.lava = 'lava'
        self.ground = 'ground'
        self.enter_one = str(input('input one from:water,air, fire, ground  ').lower())
        self.enter_two = str(input('input two from:water,air, fire, ground  ').lower())
        self.summa = None

    def __str__(self):

        return 'result is: {}'.format(self.ad())

    def input_value(self):

        return self.ad()

    def ad(self):
        self.summa = self.enter_one + self.enter_two
        if self.summa == self.water + self.fire or self.summa == self.fire + self.water:
            return self.steam
        elif self.summa == self.water + self.air or self.summa == self.air + self.water:
            return self.storm
        elif self.summa == self.water + self.ground or self.summa == self.ground + self.water:
            return self.mud
        elif self.summa == self.air + self.fire or self.summa == self.fire + self.air:
            return self.flash
        elif self.summa == self.air + self.ground or self.summa == self.ground + self.air:
            return self.dust
        elif self.summa == self.fire + self.ground or self.summa == self.ground + self.fire:
            return self.lava
        else:
            return None


a = Game()
print(a.input_value())
# print(a.__str__())
# enter_one = str(input('input one from:water,air, fire, ground  ').lower())
# enter_two = str(input('input two from:water,air, fire, ground  ').lower())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
