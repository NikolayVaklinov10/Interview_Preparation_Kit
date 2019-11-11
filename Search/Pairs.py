
import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    counter = {};
    ret = 0
    for i in arr:
        if (k + i) in counter:
            ret += counter[k + i]
        if (i-k) in counter:
            ret += counter[i-k]
        counter[i] = counter.get(i, 0) + 1
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()



