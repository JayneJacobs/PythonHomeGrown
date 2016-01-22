# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    pageIndex = content.split()
    #print pageIndex
    #print pageIndex[1]
    n=0
    for entry in pageIndex:
        keyword = entry
        #print entry
        #print keyword
        add_to_index(index,keyword,url)
        #print index
        #index = [keyword, index]
        #print index
        #return index
def lookup(index, keyword):
    for entry in index:
        if entry[0]==keyword:
            return entry[1]
        
    return[]
def add_page_to_index2(index,url,content):
    pageIndex = content.split()
    #print pageIndex
    #print pageIndex[1]
    #n=0
    for entry in pageIndex:
        keyword = entry
        #print entry
        #print keyword
        add_to_index(index,keyword,url)
        #print index
        #index = [keyword, index]
        #print index
    #return []


index = []
add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]
add_page_to_index(index,'not.test',"This is not a test")
add_page_to_index(index, 'http://dilbert.com',"""Good judgment comes from experience,
                            experience comes from bad judgement. If things aren't
                            going well it probably means you are learning a lot
                            and things will go better later --- Randy Pausch""")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


