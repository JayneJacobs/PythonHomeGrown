#!/usr/bin/python
#conditional 
print 2<3
print 1==1
print 2<3
print 1==5
print 2<3
print 1!=5
i = 21
print i
print i == 21


def absolute (x):
    if x<0:
        x=-x
    return x

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs
def bigger(first,second):
    if first < second:
        return second
    if second < first:
        return first
    if first == second:
        return second
# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs
def biggerOther(first,second):
    if second > first:
        return second
    return first
    

print absolute(-5)

print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3

print biggerOther(2,7)
#>>> 7

print biggerOther(3,2)
#>>> 3

print biggerOther(3,3)
#>>> 3