p=['Moe', 'Larry', 'Shemp']
q=p

print q
q[2]='!'

print q

print p
p[2]='Curly'

print q
q[2]='Curly'
print p
p=[0,0,7]



print p , q

spy = p

agent = spy
spy[2] = agent[2]+1
print agent , spy , q

