import numpy as np
import matplotlib.pyplot as plt

k = 0.01
x = 1.0
v = 0.0
w = 0.995
N = 1500


def xv():
    global x, v, k, w
    x += v
    v = v * w - k * x
    return x


# TM = [ n for n in range(N)]
# AR = [ xv() for n in range(N)]
AR = [xv() for n in np.arange(N)]

plt.plot(AR)
plt.show()
#print(AR)