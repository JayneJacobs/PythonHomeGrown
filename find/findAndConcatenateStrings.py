#!/usr/bin/python
#Python code t 
# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.
firstPart = s.find('u')
lastPartStart = t.find('dacious')
lastPart = t[lastPartStart:]
v = s[firstPart] + lastPart
#print firstPart
#print lastPartStart
#print lastPart
print v


