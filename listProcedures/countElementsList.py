# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.
def measure_udacity(p):
  count = 0
  for e in p:
        if e[0] == 'U':
          count = count + 1
  return count



Udacity = ['Dave','Sebastian','Katy']
print measure_udacity(Udacity)
#>>> 0
Udacity =['Umika','Umberto']
print measure_udacity(Udacity)
#>>> 2
Udacity =['Union','univercity', 'Jayne', 'UComcastU']
print measure_udacity(Udacity)
