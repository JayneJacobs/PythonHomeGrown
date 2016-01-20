#<list>.append(<element>)

stooges =['Moe','Larry','Curly']
stooges.append('Shemp')

#plus <list>+<list>
#[0,1]+[2,3] is [0,1,2,3]
#len(<list>)
#  len([0,1] is 2
# len(['a',['b',['c']]])

    
#len("Udacity") is 7
p=[1,2]
q=[3,4]
p.append(q)
print len(p)
print p

q[1]=5
print p



# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    number = 1
    for e in list_of_numbers:
        number = number * e
        
    return number
        


print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1


