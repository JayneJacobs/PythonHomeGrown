# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#
#answer_format(hours, minutes, seconds)
def convert_seconds2(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    hours = 'hour' + 's'[int(h==1):]
    minutes = 'minute' + 's'[int(m==1):]
    seconds = 'second' + 's'[int(s==1):]
    result = '{} {}, {} {}, {} {}'.format(h, hours, m, minutes, s, seconds)
    return result

def convert_seconds(seconds):
    
    secondsleft = seconds % 3600
    hours = seconds / 3600
    minutes = 0
    seconds = 0
    if secondsleft > 0:
         minutes = secondsleft / 60.00
         secondsleft = secondsleft % 60
         if secondsleft > 0:
             seconds = secondsleft
            #return answer_format(hours, minutes, seconds)

    if hours == 1:
        hour = "hour"
    if hours !=1:
        hour = 'hours'
            
    if minutes == 1:
        minute = 'minute'
    if minutes != 1:
        minute ='minutes'
   
    if seconds == 1:
        second = 'second'
    if seconds !=1: 
       second = 'seconds'
    
    answer = '{} {}, {} {}, {} {}'.format(hours, hour, minutes, minute, seconds, second)
    #print hours
    #answerlist = [hours,hour,minutes,minute,seconds,second]
    #answer = ''
    #print answerlist
    #answer = hours
    #for entry in answerlist:
        # print entry
     #   answer = answer , entry
    return answer
    #return    
def output(number, unit):
    return "{0} {1}{2}".format(number, unit, "s" if number != 1 else "")

def convert_seconds3(n):
    h, remainder = divmod(int(n), 3600)
    m = remainder / 60
    return "{0}, {1}, {2}".format(output(h, "hour"), output(m, "minute"),
                                  output(n - (3600*h + 60*m), "second"))    
print convert_seconds(3600)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds


print convert_seconds2(3600)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds2(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds2(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds3(3600)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds3(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds3(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
