# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
from lesson_005.district.soviet_street.house1 import  room1 as r11
from lesson_005.district.soviet_street.house1 import  room2 as r12
from lesson_005.district.soviet_street.house2 import  room1 as r21
from lesson_005.district.soviet_street.house2 import  room2 as r22
def room(args, x):
    print('in room number ', x)
    for i,j in enumerate(args):
        print(i,j)
    print()
room(r11.folks, 'r11')
room(r12.folks, 'r12')
room(r21.folks, 'r21')
room(r22.folks, 'r22')