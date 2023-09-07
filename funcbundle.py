def getAverage(data):
    total = 0.0
    for value in data:
        total += value
    average = format((total / len(data)), ',.2f')
    return(average)

def getMin(data):
    minimum = min(data)
    return(minimum)

def getBelowAvgCount(data , average):
    belowAvg = []
    for x in data:
        if int(x) < float(average):
            belowAvg.append(x)
    belowAvgCount = len(belowAvg)
    return(belowAvgCount)