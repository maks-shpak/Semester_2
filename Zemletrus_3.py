a = float(input('Введіть магнітуду Вашого землетрусу: '))

if 0.0 <= a <= 1.9:
    print('Ваш землетрус відноситься до: "Micro"')
elif 2.0 <= a <= 2.9:
    print('Ваш землетрус відноситься до: "Very minor"')
elif 3.0 <= a <= 3.9:
    print('Ваш землетрус відноситься до: "Minor"')
elif 4.0 <= a <= 4.9:
    print('Ваш землетрус відноситься до: "Light"')
elif 5.0 <= a <= 5.9:
    print('Ваш землетрус відноситься до: "Moderate"')
elif 6.0 <= a <= 6.9:
    print('Ваш землетрус відноситься до: "Strong"')
elif 7.0 <= a <= 7.9:
    print('Ваш землетрус відноситься до: "Major"')
elif 8.0 <= a <= 9.9:
    print('Ваш землетрус відноситься до: "Great"')
elif a >= 10.0:
    print('Ваш землетрус відноситься до: "Мeteoric"')
elif a < 0:
    print('Введенно не коректне значення')

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
