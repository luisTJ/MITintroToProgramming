import numpy
import pylab

def loadInput():

    f = open('julyTemps.txt','r')

    highs = []
    lows = []
    for line in f:
        tmp = line.split(' ')
        if(len(tmp) != 3 or not tmp[0].isdigit()):
            continue

        highs.append(int(tmp[1]))
        lows.append(int(tmp[2]))

    f.close()
    return (lows,highs)

def plot(lows,highs):
    diff = numpy.array(highs)-numpy.array(lows)

    pylab.figure("Diff");
    pylab.plot(xrange(1,32),diff)
    pylab.title("Day by Day Ranges in Temperature in Boston in July 2012")
    pylab.xlabel("Days")
    pylab.ylabel("Temperature Ranges")
    pylab.show()

(lows,highs) = loadInput()
plot(lows,highs)