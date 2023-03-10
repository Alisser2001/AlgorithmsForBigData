#Punto 4

import numpy as np

def add_lists(a,b):
    import numpy as np
    r = []
    if len(a)>=len(b):
        for i in range(len(a)):
            r.append(0)
    elif len(b)>len(a):
        for i in range(len(b)):
            r.append(0)
    if len(a)>len(b):
        for i in range(len(b)):
            r[i] = a[i] + b[i]
        for i in range(len(b), len(a)):
            r[i] = a[i]
    elif len(b)>len(a):
        for i in range(len(a)):
            r[i] = a[i] + b[i]
        for i in range(len(a), len(b)):
            r[i] = b[i]
    elif len(a)==len(b):
        for i in range(len(r)):
            r[i] = a[i]+b[i]
    return r

print(add_lists([1,4,5], [2,2]))
print(add_lists([1,4,5], [2,2,2]))
print(add_lists([1,4,5], [2,2,2,2]))