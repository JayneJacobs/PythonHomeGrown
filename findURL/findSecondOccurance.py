#!/usr/bin/python
# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.


# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(sentance,target):
    firstOccurance=sentance.find(target)
    print firstOccurance
   # secondTarget=sentance[firstOccurance + 1:]
    secondOccurance = sentance.find(target, firstOccurance + 1)
    return secondOccurance
    

#target = "De l'audace, encore de l'audace, toujours de l'audace"
    
#print find_second(first,target)

#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#print find_second(danton, 'audace')
#>>> 25

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
#>>> 13


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
#>>> 25

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
#>>> 13