import math,statistics

def computebounds(prevdata,framesize):
    if len(prevdata)<framesize:
        return None
    if len(prevdata)>framesize:
        del prevdata[0:len(prevdata)-framesize]
    m=statistics.mean(prevdata)
    v=0
    for i in prevdata:
        v+=math.pow((i-m),2)
    zscore=math.sqrt(v/framesize)*25
    highbound=prevdata[framesize-1]+zscore
    lowbound=prevdata[framesize-1]-zscore
    return [highbound,lowbound]
