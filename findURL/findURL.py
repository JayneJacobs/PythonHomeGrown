#!/usr/bin/python
#Extracting links
# # Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
startquote = page.find('"',start_link)
endlink = page.find('>', startquote+1) - 1
url = page[startquote+1:endlink]
print start_link
print startquote
print endlink
print url

