# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_lightKM = 300000. # km per second
msInseconds = 1000 # seconds ms in seconds
speed_of_lightKMms = speed_of_lightKM / msInseconds


def speed_fraction(tracems,distanceKM):
    rounddistanceKM = distanceKM * 2.0
    speedBitsms =  rounddistanceKM/tracems * 1.00000
    dataTravelKMmsRelSpOL = speedBitsms/speed_of_lightKMms
    return dataTravelKMmsRelSpOL 

print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?

print speed_fraction(16,20)
#>>> 0.00833333333333  # Any thoughts about this answer, or these inputs?
