'''関数内関数
'''

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

x = outer(3, 12)
print(x)