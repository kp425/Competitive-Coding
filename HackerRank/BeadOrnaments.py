
def isCircular(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    str1 = ' '.join(map(str, arr1))
    str2 = ' '.join(map(str, arr2))
    if len(str1) != len(str2):
        return False

    return str1 in str2 + ' ' + str2




from operator import mul
from functools import reduce

def beadOrnaments(b):
    return int((reduce(mul, map(lambda x: x ** (x - 1), b), 1) * (sum(b) ** (len(b) - 2))) % (7 + 10 ** 9))

k  = beadOrnaments([2,1])

print(k)