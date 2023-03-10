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

def empty(t):
    result = []
    for i in range(t.len()):
        result.append(t.get()) 
    return result

a = [1,4,1,10,2,3]
q = Queue()
for i in a:
    q.put(i)
k = empty(q)
print(k)