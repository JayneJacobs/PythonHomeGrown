# Loop on Lists
def print_all_elements(p):
    i=0
    while i<len(p):
        print p[i]
        i=i+1
    return p
def print_all_elements_einList(p):
    for e in p:
        print e
        
stoogeList = ["Larry", "Moe", "Shemp"]
print_all_elements(stoogeList)
print stoogeList
print "This is stoogelist using for loop e in list:"
print ' '
stoogeList.append('curly')
print_all_elements_einList(stoogeList)
print stoogeList
print ' '
myList=[1,2,[3,4]]

print_all_elements(myList)
print myList
print "This is mylist using for loop e in list:"
print ' '
print_all_elements_einList(myList)
print myList
