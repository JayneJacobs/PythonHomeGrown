# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]




#def make_big_index(index,keyword,url):
def add_to_index(index, keyword, url):
    # format of index: [[keyword, [[url, count], [url, count],..]],...]
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url,0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url,0]]])
    
def make_string(p):
    s=""
    for e in p:
        s=s+e
    return s

def make_big_index(size):

    index = []
    #index = []
    letters = ['a','a','a','a','a','a','a','a']
    while len(index)<size:
        word=make_string(letters)
        add_to_index(index,word,'fake')
        for i in range(len(letters)-1,0, -1):
            if letters[i]<'z':
                letters[i]=chr(ord(letters[i])+1)
                break
            else:
                letters[i]='a'
    return index

    
         

