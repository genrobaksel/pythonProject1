# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
sd.resolution=(1000,600)
x=150
y= 600
y1=600
point = sd.get_point(x,y)
def snowflakes (x0, lenght, y=600):
    while True:

        sd.clear_screen()
        sd.start_drawing()
        x_lambda = randint(-5, 5)
        if y < 31:
            y=31
            x_lambda=0
            sd.finish_drawing()
            return a





        point = sd.get_point(x_lambda+x0, y)
        sd.snowflake(center=point, length=lenght)
        y-=15
        pass
        pass
        sd.finish_drawing()
        sd.sleep(0.2)
        if sd.user_want_exit():
            break


x0=130
a = snowflakes(x0, lenght=20)
for i in range(N):

    snowflakes(x0, lenght=20)
    x0+=100
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


