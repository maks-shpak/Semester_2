n = int(input('Введіть число: '))

suma = 0

while n > 0:
    digit = n % 10 # ostacha
    if digit != 0:  
        suma = suma + digit
    n = n // 10 #nacilo
 
print("Сумма:", suma)

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
