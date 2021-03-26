a = []
k = 10  
for r in range(6):  
    a.append( )  
    for c in range(6):  
        a[r].append(k)  
        k += 1  
 
for r in a:
    print(r)

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")
