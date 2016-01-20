#!/usr/bin/python
###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. Make a program 
# that checks if a word is a palindrome. 
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

#word = "madam"
# test case 2
word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###
endString = len(word)
middle = len(word)/2
firstHalf = word[:middle]
secondhalf = word[middle:]
reverseSecondHalf = secondhalf[::-1]
#is_palindrome = reverseSecondHalf.find(firstHalf)
is_palindrome = word.find(reverseSecondHalf)
#letter1 = word.find(word[1],endString - 1)
#letter2 = word.find(word[2],endString - 2)
#letter4 = word.find(word[3],endString - 4)
#letter5 = word.find(word[4],endString - 5)
print firstHalf
print reverseSecondHalf
# TESTING
print is_palindrome


# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"