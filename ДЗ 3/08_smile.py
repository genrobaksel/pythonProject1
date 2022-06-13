# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution=(1000,600)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile(x,y):
    point=sd.get_point(x,y)
    sd.circle(center_position=point,radius=50,color='green',width=2)
    sd.line(sd.get_point(x - 20, y - 5), sd.get_point(x - 10, y - 20), color='green', width=2)
    sd.line(sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20), color='green', width=2)
    sd.line(sd.get_point(x + 10, y - 20), sd.get_point(x + 20, y - 5), color='green', width=2)
    sd.line(sd.get_point(x - 15, y + 20), sd.get_point(x - 15, y + 5), color='green', width=2)
    sd.line(sd.get_point(x + 15, y + 20), sd.get_point(x + 15, y + 5), color='green', width=2)


for i in range(10):
    x = sd.random_point().x
    y= sd.random_point().y

    smile(x,y)

sd.pause()
