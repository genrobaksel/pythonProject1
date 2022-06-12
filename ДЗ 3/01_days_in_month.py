# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")

if user_input == 1:
    print('Вы ввели', user_input, 'days= 31')
elif user_input == 3:
    print('Вы ввели', user_input, 'days= 31')
elif user_input == 5:
    print('Вы ввели', user_input, 'days= 31')
elif user_input == 7:
    print('Вы ввели', user_input, 'days= 31')
elif user_input == 8:
    print('Вы ввели', user_input, 'days= 31')
elif user_input == 10:
    print('Вы ввели', user_input, 'days= 31')
elif user_input == 12:
    print('Вы ввели', user_input, 'days= 31')
elif user_input == 4:
    print('Вы ввели', user_input, 'days= 30')
elif user_input == 6:
    print('Вы ввели', user_input, 'days= 30')
elif user_input == 9:
    print('Вы ввели', user_input, 'days= 30')
elif user_input == 11:
    print('Вы ввели', user_input, 'days= 30')
elif user_input == 2:

    print('Вы ввели', user_input, 'days=28')
else:
    print('error')
