# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'
def isORDNfriend(person):
    return person[0] == 'D' or person[0] == 'N'

def isDNfriend(person):
    if person[0] == 'D':
        return True
    else:
       if person[0] == 'N':
           return True
       return False
        
# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd

def is_friend(person):
    if person.find('D') == 0:
        return True
    return False

def isa_friend(person):
    return  person.find('D') == 0
       
    
name = 'Diane'
print 'Diane', is_friend(name)
#>>> True
name = 'fred'
print 'fred', is_friend(name)
#>>> False

name = 'Diane'
print isa_friend(name)

print 'Diane', is_friend('Diane')
#>>> True

print 'Fred', is_friend('Fred')
#>>> False

print "D or N"
print 'Diane', isDNfriend('Diane')
#>>> True

print 'Ned',isDNfriend('Ned')
#>>> True

print 'Moe' , isDNfriend('Moe')
#>>> False
#>>> True
name = 'fred'
print 'fred', isa_friend(name)
#>>> False

print "ORed D or N friend"
print 'Diane', isORDNfriend('Diane')
#>>> True

print 'Ned',isORDNfriend('Ned')
#>>> True

print 'Moe' , isORDNfriend('Moe')
#>>> False
#>>> True
name = 'fred'
print name , isORDNfriend(name)
#>>> False