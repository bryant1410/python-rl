
import numpy, csv, matplotlib.pyplot as plt
import sys

data = []
with open(sys.argv[1], "r") as f:
    for row in csv.reader(f):
        data += map(float, row)

data = numpy.array(data)

data2 = []
with open(sys.argv[2], "r") as f:
    for row in csv.reader(f):
        data2 += map(float, row)

data2 = numpy.array(data2)


buf = 5000
smoothed = numpy.zeros((len(data)-buf,))
smoothed2 = numpy.zeros((len(data2)-buf,))
for i in range(len(smoothed)):
    smoothed[i] = data[i:i+buf].mean()
    smoothed2[i] = data2[i:i+buf].mean()

plt.plot(smoothed)
plt.hold(True)
plt.plot(smoothed2)
plt.legend(['TDC-MSBE', 'TDC-MSPBE'])
#plt.yscale('log')
#plt.ylim([0,50])
plt.title("MSBE")
plt.xlabel("Timesteps")
plt.ylabel("Estimated MSBE")
plt.savefig("msbe.png")
#plt.show()