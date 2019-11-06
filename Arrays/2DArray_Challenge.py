import math
import os
import random
import re
import sys


def hourglassSum(arr):
    li=[]
    for i in range(len(arr)-2):

        for j in range(len(arr)-2):

          li.append(sum(arr[i][j:j+3]+arr[i+2][j:j+3])+arr[i+1][j+1])

    return max(li)



print(hourglassSum())



def hourglassSum(arr):
    return sum(arr[r - 1][c-1:c+2]) + arr[r][c] + sum(arr[r + 1][c-1:c+2])













































