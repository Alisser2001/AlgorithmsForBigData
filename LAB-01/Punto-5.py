import numpy as np

def Queue(**kwargs):
    
    def append(arr,num):
        return arr.extend([num])

    def getremove_first(arr):
        assert len(arr)!=0, "Error: Lista vacía"
        val = arr[0]
        arr.pop(0)
        return val

    class Queue__class:

        def __init__(self):
            self.elements = []

        def put(self, d):
            append(self.elements, d)

        def get(self):
            return getremove_first(self.elements)

        def len(self):
            return len(self.elements)
        
    return Queue__class(**kwargs)

def fill(t, n):
    randoms = np.random.randint(10, size = (100))
    for i in randoms:
        t.put(i)
    return t

q = fill(Queue(), 100)
print ("len =", q.len())
for _ in range(q.len()):
    print (q.get(), end=" ")