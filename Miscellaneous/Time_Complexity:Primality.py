import math

def primality(n):
    result = ["Not prime","Prime"]
    if n == 1:
        return result[0]
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return result[0]
    return result[1]

