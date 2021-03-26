a = float(input('Введіть початкову суму на вашому рахунку: '))
b = float(input('введіть річний відсоток, у вигляді 0.5 тощо: '))
c = float(input('введіть кількість років: '))

d = a *(1 + b)**c
print(round(d,2))

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
