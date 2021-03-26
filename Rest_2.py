input('Введіть назву страви: ')
a = float(input('Введіть кількість порцій: '))
b = float(input('Введіть ціну за одну порцію: '))

c = a*b
d = c*0.14 #chay
e = c*0.18 #podatok
g = c+d+e

print('Всього за страву: ', round(c,2))
print('Чайові: ', round(d,2))
print('Податок: ', round(e,2))
print('Разом: ', round(g,2))

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
