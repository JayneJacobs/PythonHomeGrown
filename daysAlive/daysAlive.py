#!/usr/bin/python
# # Write python code that defines the variable 
# age to be your age in years, andy then prints 
# out the number of days you have been alive.
agey = 57
daysInaYear = 365
birthdateMonth = 7
daysSinceBirthdayJuly = 31 - 22
newYearCurrentMonth = 1
currentDate = 6
daysleftinnewYearMonth = 31 - currentDate
newYearDays = newYearCurrentMonth * 31 - daysleftinnewYearMonth
daysSinceBirthday = ((12 - birthdateMonth) * 31) + newYearDays
daysAlive = ((agey) * daysInaYear) + daysSinceBirthday
print daysAlive
print daysSinceBirthday