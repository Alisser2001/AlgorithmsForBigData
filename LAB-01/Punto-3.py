def Stack(**kwargs):
    def append(arr, num):
        return arr.extend([num])

    def getremove_last(arr):
        assert len(arr) != 0, "Error: Lista vacía"
        val = arr[-1]
        arr.pop(-1)
        return val

    class Stack__class:

        def __init__(self):
            self.elements = []

        def put(self, d):
            append(self.elements, d)

        def get(self):
            return getremove_last(self.elements)

        def len(self):
            return len(self.elements)

    return Stack__class(**kwargs)


print("stacking elements")
s = Stack()
s.put(4)
s.put(2)
s.put("hola")
print(s.len())
print(s.elements)

print("\n--\nunstacking")
for _ in range(s.len()):
    print(s.get())
try:
    s.get()
    print("Cuidado! tu código no contiene asserts")
except AssertionError:
    print("Tu codigo está generando asserts correctos")
