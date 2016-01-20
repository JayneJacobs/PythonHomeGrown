# CostBit .50
# Latency 1s

# CPU Register .001 < 0.4 ns
# CostBit 10/2GB
# NanoDollar 10 to the -9 dollars
# DRAM 0.58 nDollars/bit 12 ns
speedoflight = 300000.00 
#2*10to the 9 * 8
def latencyDistance(sysLatency):
    LatencyDistance = speedoflight * sysLatency
    return LatencyDistance

   
HardDriveCost = 100/1*10**-9
hardDriveLatency = 7*10**-6
lightLatency = 1
print "light Latensy is",lightLatency
cpuLatency =.4 * 10**-9
dramLatency = 12*10**-9

print "CPU Latency Distance is", latencyDistance(cpuLatency)
print "hardDriveLatency Distanceis", latencyDistance(hardDriveLatency)
print "lightLatency Distance is", latencyDistance(lightLatency)
print "dramLatency Distance is", latencyDistance(dramLatency)
