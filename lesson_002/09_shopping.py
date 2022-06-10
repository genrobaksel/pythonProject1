#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
a= list(shops.keys())
a0=a[0]
a1=a[1]
a2=a[2]

cake0_n = shops['ашан'][0]['name']
cake1_n = shops['пятерочка'][0]['name']
cake2_n = shops['магнит'][0]['name']
sweet0_n = shops['ашан'][1]['name']
sweet1_n = shops['пятерочка'][1]['name']
sweet2_n = shops['магнит'][1]['name']
caramel0_n = shops['ашан'][2]['name']
caramel1_n = shops['пятерочка'][2]['name']
caramel2_n = shops['магнит'][2]['name']
pech0_n = shops['ашан'][3]['name']
pech1_n = shops['пятерочка'][3]['name']
pech2_n = shops['магнит'][3]['name']

cake0_pr = shops['ашан'][0]['price']
cake1_pr = shops['пятерочка'][0]['price']
cake2_pr = shops['магнит'][0]['price']
sweet0_pr = shops['ашан'][1]['price']
sweet1_pr = shops['пятерочка'][1]['price']
sweet2_pr = shops['магнит'][1]['price']
caramel0_pr = shops['ашан'][2]['price']
caramel1_pr = shops['пятерочка'][2]['price']
caramel2_pr = shops['магнит'][2]['price']
pech0_pr = shops['ашан'][3]['price']
pech1_pr = shops['пятерочка'][3]['price']
pech2_pr = shops['магнит'][3]['price']

shop1={'shop':a0,'price': cake0_pr},\
      {'shop':a1,'price': cake1_pr}, \
      {'shop':a2,'price': cake2_pr}
shop2={'shop':a0,'price': sweet0_pr}, \
      {'shop':a1,'price': sweet1_pr}, \
      {'shop':a2,'price': sweet2_pr}
shop3={'shop':a0,'price': caramel0_pr}, \
      {'shop':a1,'price': caramel1_pr}, \
      {'shop':a2,'price': caramel2_pr}
shop4={'shop':a0,'price': pech0_pr},\
      {'shop':a1,'price': pech1_pr},\
      {'shop':a2,'price': pech2_pr}
cakes = {cake0_n:[shop1]}
sweets = {sweet0_n:[shop2]}
caramels = {caramel0_n:[shop3]}
pechs = {pech0_n:[shop4]}
print (cakes,sweets, caramels, pechs , sep ='\n' )
#sweets = {
#    'печенье': [
#        {'shop': 'название магазина', 'price': 99.99},
        #  тут с клавиатуры введите магазины и цены (можно копипастить ;)
#    ],
    # тут с клавиатуры введите другую сладость и далее словарь магазинов
#}
# Указать надо только по 2 магазина с минимальными ценами

