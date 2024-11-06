# Ian Bullard
# UWYO COSC 1010
# Submission Date 11/05/24
# HW 03
# Lab Section: 14
# Sources, people worked with, help given to: Patrick McGrath and I worked together
# your
# comments
# here

def leap_year(year):
    if (year%4) == 0:
        if (year%100) == 0:
            return (year%400) == 0
        return True
    return False

def first_day_of_Jan(year):
    y = (year - 1)
    day_of_week = (36 + y + (y/4) - (y/100) + (y/400))%7
    return day_of_week

def valid_date(month, day, year):
    if leap_year(year) == True:
        days_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    else:
        days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    if month > 12:
        return "Invalid Date"
    else:
        month_index = (month - 1)
        if day > days_month[month_index]:
            return "Invalid Date"
        else:
            return month_index


date = input("Input a date in MM/DD/YYYY and include /\n")
split_date = date.split("/")

month = int(split_date[0])
day = int(split_date[1])
year = int(split_date[2])

month_index = valid_date(month, day, year)
print(month_index)
day_of_week = first_day_of_Jan(year)


if 0 < day_of_week < 1:
    weekday = "Sunday"
elif 1 < day_of_week < 2:
    weekday = "Monday"
elif 2 < day_of_week < 3:
    weekday = "Tuesday"
elif 3 < day_of_week < 4:
    weekday = "Wednesday"
elif 4 < day_of_week < 5:
    weekday = "Thursday"
elif 5 < day_of_week < 6:
    weekday = "Friday"
elif day_of_week > 6:
    weekday = "Saturday"

print(weekday)


