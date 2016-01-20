# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element_while(p,val):
  i = 0
  while i < len(p):
    if p[i] == val:
      return i
    i = (i + 1)
    #print value
      
  return -1
def find_element_for(p,val):
  i = 0
  for e in p:
    if e == val:
      return i
    i = (i + 1)
    #print value
      
  return -1

print "Using a while Loop"
myList = [1,2,3]
target = 3
print "this is an element of 3"
print find_element_while(myList,target)
#>>> 2
myList = ['alpha','beta']
print myList
print "there is an element of gamma"
target = 'gamma'
print find_element_while(myList,target)
#>>> -1

print "Using a for Loop"
myList = [1,2,3]
target = 3
print "this is an element of 3"
print find_element_for(myList,target)
#>>> 2
myList = ['alpha','beta']
print myList
print "there is an element of gamma"
target = 'gamma'
print find_element_for(myList,target)
#>>> -1
