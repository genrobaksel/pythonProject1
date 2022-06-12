# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1000, 500)

step=500
def brik(x, y):
    left = sd.get_point(x, y)
    right = sd.get_point(x + 100, y + 50)
    sd.rectangle(left_bottom=left, right_top=right, color='red', width=1)


for x in range(-step, 1000, 100):
    for y in range(0, step, 50):
        brik(x, y)
        x += 50

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


sd.pause()
