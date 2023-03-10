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

print ("enqueueing elements")
q = Queue()
q.put(4)
q.put(2)
q.put("hola")
print (q.len())
print (q.elements)

print ("\n--\ndequeueing")
for _ in range(q.len()):
    print (q.get())

print ("this next call must fail")
try:
    q.get()
    print ("Cuidado! tu código no contiene asserts")
except AssertionError:
    print ("Tu codigo está generando asserts correctos")