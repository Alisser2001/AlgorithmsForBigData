def getremove_last(x):
    assert len(x)!=0, "Error: Lista vacía"
    val = x[-1]
    x.pop(-1)
    return val, x
try:
    x = [1,5,6]
    print ("initial", x)
    for i in range(len(x)+1):
        val, x = getremove_last(x)
        print ("last val", val, ", remaining list", x)
    print ("*** cuidado! tu código no contiene asserts")
except AssertionError:
    print ("Tu codigo está generando asserts correctos")


