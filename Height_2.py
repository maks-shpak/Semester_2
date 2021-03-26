from math import floor


height = int(input("Enter your height in cm: "))
foot = floor(height / 30.48)
inch = floor(height / 2.54 - (12 * foot))
print(f"Your height: {foot} foot, {inch} inches.")


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Макс Шпак")

