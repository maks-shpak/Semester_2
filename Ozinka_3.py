n = input('Введіть вашу буквенну оцінку: ')

if n == 'F' or n == 'f':
    print('Ваша оцінка: 0')
elif n == 'D' or n == 'd':
    print('Ваша оцінка: 1.0')
elif n == 'D+' or n == 'd+':
    print('Ваша оцінка: 1.3')
elif n == 'C-' or n == 'c-':
    print('Ваша оцінка: 1.7')
elif n == 'C' or n == 'c':
    print('Ваша оцінка: 2.0')
elif n == 'C+' or n == 'c+':
    print('Ваша оцінка: 2.3')
elif n == 'B-' or n == 'b-':
    print('Ваша оцінка: 2.7')
elif n == 'B' or n == 'b':
    print('Ваша оцінка: 3.0')
elif n == 'B+' or n == 'b+':
    print('Ваша оцінка: 3.3')
elif n == 'A-' or n == 'a-':
    print('Ваша оцінка: 3.7')
elif n == 'A' or n == 'a':
    print('Ваша оцінка: 4.0')
elif n == 'A+' or n == 'a+':
    print('Ваша оцінка: >4.0')
else:
    print('Введенно не коректну буквенну оцінку')

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")






