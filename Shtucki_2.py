a=int(input('Введіть кількість штучок яку ви хлчете придбати: '))
b=int(input('Введіть кількість штукенцій яку ви хочете придбати: '))

c = a*75
print('Вага штучок', c)
d= a * 112
print('Вага штукенцій', d)
h = c + d
print('Повна вага вашого замовлення: ', h)

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
