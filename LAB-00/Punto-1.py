import numpy as np

def suma_matrices(a,b):
    final = []
    for i in range(len(a)):
        arr1 = a[i]
        arr2 = b[i]
        arrSum = []
        for j in range(len(arr1)):
            arrSum .append(arr1[j] + arr2[j])
        final.append(arrSum)
    return final

a = np.random.randint(10, size=(3,2))
b = np.random.randint(10, size=(3,2))
print (a)
print (b)
print ("---resultado----\n",suma_matrices(a,b))