# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
Kilb = 2 ** 10  #
KilB = 8 * Kilb #bits 
Megb = 2 ** 20  #bits
MegB = 8 * Megb   #
Gigb = 2 ** 30   #bits
GigB = 8 * Gigb   #
Terab = 2 ** 40 #bits
TeraB = 8 * Terab  #

def output(number, unit):
    return "{0} {1}{2}".format(number, unit, "s" if number != 1 else "")

def convert_seconds(n):
    h, remainder = divmod(int(n), 3600)
    m = remainder / 60
    return "{0}, {1}, {2}".format(output(h, "hour"), output(m, "minute"),
    
                                  output(n - (3600*h + 60*m), "second"))
def get_bandwidth(b,bUnit):
    if bUnit == 'kb':
       bandwidth = b*Kilb * 1.00
    if bUnit == 'kB':
       bandwidth = b*KilB  * 1.00
    if bUnit == 'Mb':
       bandwidth = b*Megb  * 1.00
    if bUnit == 'MB':
       bandwidth = b*MegB  * 1.00
    if bUnit == 'Gb':
       bandwidth = b*Gigb  * 1.00
    if bUnit == 'GB':
       bandwidth = b*GigB * 1.00
    if bUnit == 'Tb':
       bandwidth = b*Terab * 1.00
    if bUnit == 'TB':
       bandwidth = b*TeraB * 1.00
    return bandwidth


def get_filesize(f,fUnit):
    if fUnit == 'kb':
       filesize = f*Kilb * 1.00
    if fUnit == 'kB':
       filesize = f*KilB * 1.00
    if fUnit == 'Mb':
       filesize = f*Megb * 1.00
    if fUnit == 'MB':
       filesize = f*MegB * 1.00
    if fUnit == 'Gb':
       filesize = f*Gigb * 1.00
    if fUnit == 'GB':
       filesize = f*GigB * 1.00
    if fUnit == 'Tb':
       filesize = f*Terab * 01.00
    if fUnit == 'TB':
       filesize = f*TeraB * 01.00
    return filesize
    
def download_time(fs,fsUnit,bw,bwUnit):
   # seconds = 0
    seconds = get_filesize(fs,fsUnit)/get_bandwidth(bw,bwUnit)
   
    #seconds = get_bandwidth(bw,bwUnit)/get_filesize(fs,fsUnit) * 1.0
    print seconds , 'seconds'
    answer = convert_seconds(seconds)
    return answer
    
    
print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#>>>0 hours, 37 minutes, 32.8 seconds

print download_time(1,'Tb', 100, 'MB')
#>>>0 hours, 37 minutes, 32.8 seconds
