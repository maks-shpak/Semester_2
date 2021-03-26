print("{0:>35}{1:>15}".format('Цельсій', 'Фаренгейт'))

a = 0 # 0 celsius
b = 32 # 0 celsius
print("{0:>32}{1:>15}".format(a, b))
print("{0:>32}{1:>15}".format(a+10, b+18))
print("{0:>32}{1:>15}".format(a+20, b+36))
print("{0:>32}{1:>15}".format(a+30, b+54))
print("{0:>32}{1:>15}".format(a+40, b+72))
print("{0:>32}{1:>15}".format(a+50, b+90))
print("{0:>32}{1:>15}".format(a+60, b+108))
print("{0:>32}{1:>15}".format(a+70, b+126))
print("{0:>32}{1:>15}".format(a+80, b+144))
print("{0:>32}{1:>15}".format(a+90, b+162))
print("{0:>32}{1:>15}".format(a+100, b+180))

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
