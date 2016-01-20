def replace_spy(spy):
  spy2 = spy
  spy2[2]=spy[2]+1
  # print spy
  #return spy2
  
# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.
spy = [0,0,7]
replace_spy(spy)
print spy
#>>> [0,0,8]
