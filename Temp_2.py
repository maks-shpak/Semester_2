a = int(input('Введіть температуру в градусах по Цельсію: '))
b = a + 273.15
c = a*1.8+32.0
print('Температура по Кельвіну: ', b)
print('Температура по фаренгейту: ',c)

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
