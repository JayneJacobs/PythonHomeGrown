#!/usr/bin/python
# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def square(a):
    c = a * a
    return c
    
def sum3(a,b,c):
    return a + b + c
    
def abbaize(aword,bword):
    return aword + (bword * 2) + aword
    
aword = 'oh'
bword = 'my'
print abbaize(aword, bword)


a = 10
y = square(a)
print square(y)
print a

b = y
c = 30
print sum3(a,b,c)
print a
# To test your procedure, uncomment the print 
# statement below, by removing the hash mark (#) 
# at the beginning of the line.

# Do not remove the # from in front of the line 
# with the arrows (>>>). Lines which begin like 
# this (#>>>) are included to show the results
# you should see when run your procedure.

