
# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.
#n (n - i)
#4(4-3)
# that number.
#n (n - i)
#4(4-3)

def printNumbers(n):
    i=1
    while i<=n:
        print i 
        i=i+1
def printNumbers1(n):
    i=1
    while True:
        if i>n:
            break
        print i 
        i=i+1
    

def factorial(n):
 i = n
 factor = n
 if n == 0:
  factor = 1
 else:
  while i > 1:
   i = i - 1
   factor = (n - i) * factor 
 return factor
print " the factorial of 4 is" 
print factorial(4) 
#>>> 24
print "the factorial of 5 is"
print factorial(5)
#>>> 120
print "the factorial of 6 is"
print factorial(6)
#>>> 720
print factorial(1)
print factorial(0)
print factorial(10)
print "breaks"
printNumbers1(5)
print "1 is done"
   
printNumbers(7)
    