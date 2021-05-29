def leapYear(year):
    if year%4 != 0:
        return False
    if year%100 != 0:
        return True
    return (year%400 == 0)

def numDays (year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if leapYear(year):
        return 29
    else:
        return 28


def dayOfWeek(year, month, day):
    counter = 0

    # step 1: count the number of days from 2000 to year-1


    # step 2: count the number of days from year/Jan to year/(month-1)


    # step 3: count the number of days from year/month/1 to year/month/(day-1)

    n = counter%7
    if n==0:
        return "Sat"
    # step 4: complete the code for the other cases


print(dayOfWeek(2001,1,28))   # Sun
print(dayOfWeek(2002,11,21))  # Thu
print(dayOfWeek(2004,3,4))    # Thu
print(dayOfWeek(2008,7,1))    # Tue
print(dayOfWeek(2011,5,8))    # Sun
print(dayOfWeek(2013,3,23))   # Sat
