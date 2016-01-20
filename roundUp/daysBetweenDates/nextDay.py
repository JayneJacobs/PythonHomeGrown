###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###
# A.  write stub daysInMonth(year, month) that returns 30
# B.modify nextDay(year, month, day) to use daysInMonth(year, month)
# C. test nextDay(year, month, day) using stub daysInMonth
# D. modify days InMonth(year, month) to be correct except for leap years
# E. test nextDay(year, month, day) using stub daysInMonth
# F. write isLeapYear(year)
# G. test isLeapYear(year)
# K. Test daysBetweenDates for all cases

def nextDayAlt(year, month, day):
  #  """
  #  Returns the year, month, day of the next day.
   # Simple version: assume every month has 30 days.
    #"""
   
  if day<30:
    return year, month, day+1
  else:
    if month<12:
      return year, month+1,1
    else:
      return year+1, 1, 1
    
def nextDay(year, month, day):
  #  """
  #  Returns the year, month, day of the next day.
   # Simple version: assume every month has 30 days.
    #"""
   
  if day == 30:
    day2 = 1
    if month == 12:
       month2 = 1
       year2 = year + 1
    else:
        month2 = month + 1
        year2 = year
    return year2, month2, day2
  else:
    day2 = day + 1
    year2 = year
    month2 = month
  return year2, month2, day2
    
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """returns True of year1-month1-day1 is before year2-month2-day2 otherwise returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
            if month1 < month2:
                return True
            if month1 == month2:
                return day1 < day2
    return False       
       
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
     year1, month1, day1 = nextDay(year1, month1, day1)
     days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args) 
  
    
print nextDay(1999, 12, 30)
print nextDay(1999, 12, 30)
print nextDay(2013, 1, 30)
print nextDay(2012, 12, 30)
print nextDay(2000, 1, 1)
print nextDay(2013, 2, 1)
print nextDay(2013, 1, 1)

print "This is the Alternate Method"
print nextDayAlt(1999, 12, 30)
print nextDayAlt(1999, 12, 30)
print nextDayAlt(2013, 1, 30)
print nextDayAlt(2012, 12, 30)  
print nextDayAlt(2000, 1, 1)
print nextDayAlt(2013, 2, 1)
print nextDayAlt(2013, 1, 1)


print "This is the daysBetweenDates"
test()
