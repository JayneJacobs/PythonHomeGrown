# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(lsta,lstb):
  #i = 0
  #lstc = lsta
  for e in lstb:
    lstc = lsta
    if (e not in lsta):
      print e
      lsta.append(e)
      #lsta = lstc + e
      #print lsta + lstb[i]
    #lstc = lsta
   # i = i + 1
  return lsta
  
# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
#a = ['one','two','three']
#b= ['two','four','six']
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
