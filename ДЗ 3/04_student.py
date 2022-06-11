# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses, procent = int(100),int(1000), int(1)
def for_10_manths(x, y):
    x1=0
    for j in range(10):
        x += int(x * y/100)
        x1+=x
    return x1

a = for_10_manths(expenses, procent)
print(a)
egsumm = educational_grant*10
any_expenses = int()
i=int()
while i < a:
    any_expenses+=1
    i = egsumm + any_expenses
print(any_expenses)
