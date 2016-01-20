#!/usr/bin/python
#while loops
def testingwhile(i):
    while i < 10:
        print i
        i = i + 1
    print 'i is now', i
    return i
def testingwhile2(i):
    while i != 10:
        print i
        i = i + 1
    print 'i is now', i
    return i    
print 'i=1'   
testingwhile2(1)
print 'i=0'
testingwhile2(0)

print 'i is now', testingwhile2(0)
