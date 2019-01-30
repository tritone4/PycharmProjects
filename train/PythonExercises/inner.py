'''関数内関数
'''
import numpy as np

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

x = outer(3, 12)
print(x)

Z = np.zeros(10)
print(Z)