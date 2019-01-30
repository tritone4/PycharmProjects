"""
Matplotlibの練習
"""
import numpy as np
import matplotlib.pyplot as plt
import math as math

# データの作成
#x = np.arange(0, 6, 0.1)
#y = np.sin(x)
#
#plt.plot(x, y)
#plt.show()

#def e_calc(n):
#    return (1 + 1/n)**n
#
#x = [ e_calc(n+1) for n in range(50)]
## print(x)
#
#plt.plot(range(50), x)
#plt.show()

def circ(m):
    th = math.pi / m
    return math.sin(th) * m

b = [circ(2**n) for n in range(2,10,1)]

print(b)
plt.plot(range(2,10,1), b)
plt.show()



