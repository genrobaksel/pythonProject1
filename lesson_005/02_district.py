# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from lesson_005.district. central_street.house1 import room1 as rc11
from lesson_005.district. central_street.house1 import room2 as rc12
from lesson_005.district. central_street.house2 import room1 as rc21
from lesson_005.district. central_street.house2 import room2 as rc22
from lesson_005.district.soviet_street.house1 import  room1 as rs11
from lesson_005.district.soviet_street.house1 import  room2 as rs12
from lesson_005.district.soviet_street.house2 import  room1 as rs21
from lesson_005.district.soviet_street.house2 import  room2 as rs22
from lesson_005 import district as distr
def district(*args):
    print('На районе живут ...')
    print()
    for i in args:
        if i==[]:
            continue
        a = ','.join(i)
        print(a)
district(rc11.folks, rc12.folks, rc21.folks, rc22.folks, rs11.folks, rs12.folks, rs21.folks, rs22.folks)



