# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.
def biggerOther(first,second):
    if second >= first:
        return second
    return first
def biggest3(a,b,c):
    return biggerOther(biggerOther(a,b),c)
    
def biggest(num1,num2,num3):
    if num1 >= num2 and num1 >= num3: 
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    if num3 >= num1 and num3 >= num2:
        return num3  

def biggest2(a,b,c):
 if a > b and a > c:
  return a
 else:
  if b > a and b > c:
   return b
  else:
   if c >= a and c >= b:
    return c
   else:
     if c >= a and a == b:
      return c
     else:
      if a >= c and c == b:
       return a
      else:
       if b >= a and c == a:
        return b
       else:
        if a >= b and c == a:
         return a
        else:
         if a == b and a >= c:
          return a
   

print 'biggest'    
print biggest(3, 3, 9), ' 3, 3, 9'
#>>> 9

print biggest(6, 9, 3), '(6, 9, 3) '
#>>> 9

print biggest(9, 3, 6), '(9, 3, 6)'
print biggest(9, 9, 6), '(9, 9, 6)'
print biggest(6, 9, 9), '(6, 9, 9)'
print biggest(1, 1, 1), '(1, 1, 1)'
#>>> 9
print 'biggest2'
print biggest2(3, 3, 9), ' 3, 3, 9'
#>>> 9

print biggest2(6, 9, 3), '(6, 9, 3) '
#>>> 9

print biggest2(9, 3, 6), '(9, 3, 6)'
print biggest2(9, 9, 6), '(9, 9, 6)'
print biggest2(6, 9, 9), '(6, 9, 9)'
print biggest2(1, 1, 1), '(1, 1, 1)'
#>>> 9
print 'biggest3'
print biggest3(9, 3, 6), '(9, 3, 6)'
print biggest3(9, 9, 6), '(9, 9, 6)'
print biggest3(6, 9, 9), '(6, 9, 9)'
print biggest3(1, 1, 1), '(1, 1, 1)'
#>>> 9