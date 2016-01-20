#!/usr/bin/python
# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
#x = 3.5 
# >>> 4 (not 4.0)

x = 9.14159

#ENTER CODE BELOW HERE
dotx = str(x).find('.')
decimal = str(x)[dotx+1]
round5 = decimal.find('5')
round6 = decimal.find('6')
round7 = decimal.find('7')
round8 = decimal.find('8')
round9 = decimal.find('9')
y = round9 * round8 * round7 * round6 * round5
z = x + y + 1
dotz = str(z).find('.')
whole = str(z)[:dotz]
#print z
#print decimal
#print round5
#print dotx
print whole














