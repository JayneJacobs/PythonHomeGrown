distanceKM = 4300
speedLightKMS = 300000.00
bitTimeS = .10
speedBitsKMS = 4300.00 * 2/bitTimeS
lightTimeS = distanceKM/speedLightKMS
TimeforTravReltoLight = bitTimeS/lightTimeS
fractionS = speedBitsKMS/speedLightKMS#bitTime = distance/speedBits

print 1/7.0
print TimeforTravReltoLight
print lightTimeS
print bitTimeS
print fractionS

