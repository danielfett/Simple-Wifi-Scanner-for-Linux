import sys
import math
channel_usage = {}
for line in sys.stdin:
    if line.strip().startswith("Channel"):
        channel = int(line.split(':')[-1].strip())
    if line.strip().startswith("Quality"):
        signal = int(line.split('=')[-1].split(' ')[0])
        watts = math.pow(10,(signal/10.0))*0.001
        if channel in channel_usage:
            channel_usage[channel]['watts'] += watts
        else:
            channel_usage[channel] = {'watts': watts}
            
for i in range(1,14):
    if not i in channel_usage:
        print "%4d: |" % i
    else:
        dbm = 10*math.log(channel_usage[i]['watts']/0.001, 10)
        length = int((dbm+90)*0.5)
        print "%4d: |%s" % (i, "#"*length)
        
        
