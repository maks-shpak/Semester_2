b = float(input('Введіть кількість хлібу котрий ви хочете придбати: '))

c = 8.50 * b #svizhak
d = c * 0.6 #vchorashka scidka

g = c - d #suma vchorashki


print("{0:>50}".format(round(c,2)))
print("{0:>50}".format(round(d,2)))
print("{0:>50}".format(round(g,2)))

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
