# -*- coding: utf-8 -*-

import simple_draw

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
simple_draw.resolution= (1200,700)

import simple_draw
simple_draw.resolution = (1200, 600)
def branch(point, angle, length, width):
    if length < 10:
        return
    vector = simple_draw.Vector(point, angle, length, width)
    vector.draw(simple_draw.random_color())
    branch(vector.end_point, angle - 30, length * 0.8, width)
    branch(vector.end_point, angle + 30, length * 0.8, width)
point = simple_draw.get_point(600, 5)

angle, length, width = 90, 100,3
branch(point, angle, length, width)
simple_draw.pause()
# for i in range(10):
#     angle-=30
#     lenght=lenght/2
#     a = sd. get_vector(start_point=a.end_point,angle=angle, length= lenght, width=width)
#     a.draw()
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()




