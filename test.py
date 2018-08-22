import matplotlib.pyplot as plt
import numpy as np
from numpy import fft
import scipy.integrate as integrate
import scipy.special as special

f = open("chan", 'r')
contents = f.read().split("\n")

datapoints = {}
for row in contents:
    if "#" in row:
        continue
    datapoint = row.split()
    if len(datapoint) < 4:
        continue
    if datapoint[1] in datapoints:
        datapoints[datapoint[1]].append(datapoint[3])
    else:
        datapoints[datapoint[1]] = [datapoint[3]]

Fs = 256 #Sampling rate of EEG
Ts = 1/Fs

afz = datapoints["AFZ"]
n = len(afz)

k = np.arange(n)
T = n/Fs
freq = k/T
freq = freq[range(n/2)]

y = np.fft.fft(afz)/n
y = y[range(n/2)]

plt.figure(1)
#plt.subplot(2,1,1)
ax = plt.gca()
ax.plot(freq, abs(y))
ax.set_xlabel("Frequency [Hz]")
ax.set_ylabel("|Y(freq)|")
#plt.subplot(2,1,2)
#ax2 = plt.gca()
#ax2.plot(afz)
plt.show()

#print(freq)
#print(abs(y))
# Integral section
ratio1_numerator = abs(y)[1, 20].sum()
ratio1_denomenator = abs(y)[1, 100].sum()
ratio2_numerator = abs(y)[5, 10].sum()
ratio2_denominator = abs(y)[1, 4].sum()

print(ratio1_numerator/ratio1_denominator)
print(ratio2_numerator/ratio2_denominator)
