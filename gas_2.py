p = int(input("Введіть тиск(Па): "))
v = int(input("Введіть об'єм(Л): "))
t = int(input("Введіть температуру: "))
t = t + 273.15
R = 8.314
#v = v / 1000
n = ( p * v ) / ( R * t )
print("Молярна маса становить: ", n)

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
