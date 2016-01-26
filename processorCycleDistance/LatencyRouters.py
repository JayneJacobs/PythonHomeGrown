tRndTrpBE_SWEDms = 75.00
distanceKM = 2500.00 * 2.00
msPersecond = 1000.00
spOLtFiberKMS = 200000.00
spOLtFiberKMms = spOLtFiberKMS * 1/msPersecond
tEnroutems = distanceKM  / spOLtFiberKMms
tRouters = tRndTrpBE_SWEDms - tEnroutems

print tRouters, 'is time at routers'
print spOLtFiberKMms, 'is spd of light in ms'
print tEnroutems, 'is timeEnroute'
