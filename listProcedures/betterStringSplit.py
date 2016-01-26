# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    separatorIndex = []
    wordIndex = []
    atsplit = True #at split point
    #print splitlist
    #print splitlist[1]
    print len(splitlist)
    n = 0
    w = 0
    
        
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                wordIndex.append(char)
                atsplit = False
            else:
                #addcharacter to last word
                wordIndex[-1] = wordIndex[-1] + char
        out = wordIndex         
   # for entry in separatorIndex:
   #     word = source[source.find(separatorIndex[w]:
   #     w = w + 1
        
        
        #append.wordIndex(word)
    
    while n < len(splitlist):
        element = splitlist[n]
        #print element
        separatorIndex.append(element)
        n = n+1
    return out, separatorIndex
   # source.find(splitlist.
   # for 


out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

#out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
#print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
