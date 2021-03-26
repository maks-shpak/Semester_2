a = int(input('Введіть свій людський вік: '))

b = a * 7

print('За першим правилом вам ', b, 'Собачих років')

c = 2 * 10.5
d = ((a - 2) * 4) + c

print('За другим правилом вам ', d,  'Собачих років')

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
