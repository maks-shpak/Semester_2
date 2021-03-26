a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))

while a != 0 and b != 0:
    if a > b:
        a = a % b #більше число заміняємо остачею від ділення
                  #далі знову ділимо більше на менше доки не вийде 0
                  #в одній із змінних виходить нуль тоді інше число є НСК, тому записуємо сумою
    else:
        b = b % a

print('НСК ваших чисел: ',a + b)

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
