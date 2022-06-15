# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()



# print(color_0)
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
sd.resolution=(800,600)
def col (color):
    ar = int(input('enter expect color'))
    for i,j in enumerate(color):
        if i == ar:
            return j

color =[sd.COLOR_RED,sd.COLOR_ORANGE,sd.COLOR_YELLOW,sd.COLOR_GREEN,sd.COLOR_CYAN,sd.COLOR_BLUE,sd.COLOR_PURPLE]
colors = ['red', 'blue', 'green', 'black']
color_01=col(color=color)

def lines(length, z):
    a = sd.get_point(350, 100)
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
lines(110, 10)

sd.pause()
