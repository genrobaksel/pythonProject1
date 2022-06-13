# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution= (1000,600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
def lines (x,y, color):

    left = sd.get_point(x, y)
    right = sd.get_point(x+300,y+400)
    sd.line(start_point=left, end_point=right, color=color, width=4)

def circle_lines (x1,y1,color):
    center = sd.get_point(x1, y1)

    sd.circle(center_position=center, radius=radius,color=color, width=6)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

x=50
y=50
for i in rainbow_colors:
    y-=5
    a= lines(x,y, color=i)
radius=340


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
for j in rainbow_colors:
    radius-=6
    b=circle_lines(500,-40,color=j)

sd.pause()
