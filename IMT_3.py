print('Введіть цифру 1 якщо ви будете вводити масу в "кілограмах" та зріст в "метрах"')
print('Введіть циру 2 якщо ви будете вводити масу в "фунтах" та зріст в "дюймах"')

n = int(input('Введіть цифру: '))

if n == 1:
    a = float(input('Введіть свій зріст(М, у вигляді 1.65): '))
    b = float(input('Введіть свою масу(КГ): '))
    c = b / (a**2)
    print('Ваше ІМТ: ', round(c, 2))
    
elif n == 2:
     a = float(input('Введіть свій зріст(Дюйми): '))
     b = float(input('Введіть свою масу(Фунти): '))
     c = 703 * (b / (a**2))
     print('Ваше ІМТ: ', round(c, 2))

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
