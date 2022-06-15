# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

sd.resolution=(800,600)

def trangle(angle, length):
    a = sd.get_point(200, 300)
    v1=sd.get_vector(start_point=a, angle=angle, length=length, width=3)
    v1.draw(color='red')
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+120, length=length, width=3)
    v2.draw(color='red')
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw(color='red')
def squareangle(angle, length):
    a = sd.get_point(510, 300)
    v1=sd.get_vector(start_point=a, angle=angle, length=length, width=3)
    v1.draw(color='red')
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90, length=length, width=3)
    v2.draw(color='red')
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw(color='red')
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw(color='red')
def fiveangle(angle, length):
    a = sd.get_point(510, 300)
    v1=sd.get_vector(start_point=a, angle=angle, length=length, width=3)
    v1.draw(color='red')
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90, length=length, width=3)
    v2.draw(color='red')
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw(color='red')
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw(color='red')
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 270, length=length, width=3)
    v5.draw(color='red')

point = sd.get_point(350, 100)

def lines( length, point,angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color='red')
    return v1.end_point

def n_fig_angls(z):
    n_angls=360/z

    length=100
    angle_0=0
    next_length = length
    next_angle=angle_0
    a = point
    for i in range(z):
        a=lines(length=next_length,point=a,angle=next_angle )
        next_angle+=n_angls

n_fig_angls(7)
#     a1=lines(length=next_length,point=a,angle=angle_0)
#      angle_0+=n_angls
#      a2=lines(length=next_length,point=a1,angle=angle_0 )

def lines( length,  z):
     a = sd.get_point(350, 100)
     angle_0=0
     next_angl=angle_0
     n_angls = 360 / z
     b = sd.get_vector(start_point=a, angle=next_angl, length=length, width=3)
     b.draw(color='red')
     z1=z-1
     for i in range(z1):
         next_angl += n_angls
         b = sd.get_vector(start_point=b.end_point, angle=next_angl , length=length, width=3)
         b.draw(color='red')

lines(110,9)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
