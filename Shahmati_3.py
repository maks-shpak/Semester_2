n = input('Введіть букву колонки: ')

if n == 'a' or n == 'A':
    m = int(input('Введіть номер рядка: '))
    if m == 1 or m == 3 or m == 5 or m == 7:
        print('Колір цієї клітинки: Чорний')
    elif m == 2 or m == 4 or m == 6 or m == 8:
        print('Колір цієї клітинки: Білий')
        
elif n == 'b' or n == 'B':
    m = int(input('Введіть номер рядка: '))
    if m == 1 or m == 3 or m == 5 or m == 7:
        print('Колір цієї клітинки: Білий')
    elif m == 2 or m == 4 or m == 6 or m == 8:
        print('Колір цієї клітинки: Чорний')
        
elif n == 'с' or n == 'С':
    m = int(input('Введіть номер рядка: '))
    if m == 1 or m == 3 or m == 5 or m == 7:
        print('Колір цієї клітинки: Чорний')
    elif m == 2 or m == 4 or m == 6 or m == 8:
        print('Колір цієї клітинки: Білий')

elif n == 'd' or n == 'D':
    m = int(input('Введіть номер рядка: '))
    if m == 1 or m == 3 or m == 5 or m == 7:
        print('Колір цієї клітинки: Білий')
    elif m == 2 or m == 4 or m == 6 or m == 8:
        print('Колір цієї клітинки: Чорний')
        
elif n == 'e' or n == 'E':
    m = int(input('Введіть номер рядка: '))
    if m == 1 or m == 3 or m == 5 or m == 7:
        print('Колір цієї клітинки: Чорний')
    elif m == 2 or m == 4 or m == 6 or m == 8:
        print('Колір цієї клітинки: Білий')

elif n == 'f' or n == 'F':
    m = int(input('Введіть номер рядка: '))
    if m == 1 or m == 3 or m == 5 or m == 7:
        print('Колір цієї клітинки: Білий')
    elif m == 2 or m == 4 or m == 6 or m == 8:
        print('Колір цієї клітинки: Чорний')

elif n == 'g' or n == 'G':
    m = int(input('Введіть номер рядка: '))
    if m == 1 or m == 3 or m == 5 or m == 7:
        print('Колір цієї клітинки: Чорний')
    elif m == 2 or m == 4 or m == 6 or m == 8:
        print('Колір цієї клітинки: Білий')

elif n == 'h' or n == 'H':
    m = int(input('Введіть номер рядка: '))
    if m == 1 or m == 3 or m == 5 or m == 7:
        print('Колір цієї клітинки: Білий')
    elif m == 2 or m == 4 or m == 6 or m == 8:
        print('Колір цієї клітинки: Чорний')

else:
    print('Введенно не коректнно букву стовпчика')


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
