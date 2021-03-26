a = int(input('Введіть кількість днів: '))

b = int(input('Введіть кількість годин: '))
if b > 24:
     print('Введенно не коректне значення')
     b = int(input('Введіть кількість годин: '))
     
c = int(input('Введіть кількість хвилин: '))
if c > 60:
    print('Введенно не коректне значення')
    c = int(input('Введіть кількість хвилин: '))
    
d = int(input('Введіть кількість секунд: '))
if d > 60:
     print('Введенно не коректне значення')
     d = int(input('Введіть кількість секунд: '))
     
q = a * 86400 #days
w = b * 3600 #hour
e = c * 60 # min
r = q + w + e + d

print('У цьому проміжку ', r, ' Секунд')

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
