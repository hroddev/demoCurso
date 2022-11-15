def isLeapYear(year):
    if year % 400 == 0:
        print(year,"es un año bisiesto")
    elif year % 4 == 0 and year % 100 != 0:
        print(year,"es un año bisiesto")
    else:
        print(year,"no es un año bisiesto")

isLeapYear(2005)