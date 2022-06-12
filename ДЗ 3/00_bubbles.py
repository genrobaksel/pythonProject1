# -*- coding: utf-8 -*-

import simple_draw as sd

import simple_draw as sd
import  random


sd.resolution= (1200,600)
i =4

for x in range(100,400,100):

    for k in range(100,1100,100):
        point = sd.get_point(k, x)
        radius = 55
        for j in range(3):
            radius+=10
            sd.circle(center_position=point,radius= radius,color='red')
for _  in range (100):
    point = sd.random_point()
    radius = 55
    for j in range(3):
        radius = random.randint(5,40)
        sd.circle(center_position=point, radius=radius, color='red')
sd.pause()
#while i<5:
#    sd.circle(center_position=point, radius=radius, color='red')




