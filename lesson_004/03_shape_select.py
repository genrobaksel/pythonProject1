# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution=(800,600)
def col (colors):
    ar = int(input('enter expect color'))
    for i,j in enumerate(colors):
        if i == ar:
            return j

color =[sd.COLOR_RED,sd.COLOR_ORANGE,sd.COLOR_YELLOW,sd.COLOR_GREEN,sd.COLOR_CYAN,sd.COLOR_BLUE,sd.COLOR_PURPLE]
colors = ['red', 'blue', 'green', 'black']
color_01=col(colors=color)

def lines(length, x=350, y=200):
    t = int(input('enter item angle for figure'))
    z=t+3
    a = sd.get_point(x, y)
    angle_0 = 0
    next_angl = angle_0
    n_angls = 360 / z
    b = sd.get_vector(start_point=a, angle=next_angl, length=length, width=3)

    b.draw(color=color_01)
    z1 = z - 1
    for i in range(z1):
        next_angl += n_angls
        b = sd.get_vector(start_point=b.end_point, angle=next_angl, length=length, width=3)

        b.draw(color=color_01)
lines(200)





sd.pause()

