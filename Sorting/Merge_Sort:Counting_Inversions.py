import os

# Complete the countInversions function below.
def merge_sort(sort_list):
    len_list = len(sort_list)
    if len_list > 1:
        mid = len_list // 2
        leftHalf = sort_list[:mid]
        rightHalf = sort_list[mid:]
        merge_sort(leftHalf)
        merge_sort(rightHalf)
        merging(leftHalf, rightHalf, sort_list)


def merging(leftHalf, rightHalf, sort_list):
    i = 0
    j = 0
    k = 0
    left_len = len(leftHalf)
    right_len = len(rightHalf)
    while i < left_len and j < right_len:
        if leftHalf[i] <= rightHalf[j]:
            sort_list[k] = leftHalf[i]
            i += 1
        else:
            sort_list[k] = rightHalf[j]
            j += 1
            global count
            count += left_len - i
        k += 1

    while i < left_len:
        sort_list[k] = leftHalf[i]
        i += 1
        k += 1

    while j < right_len:
        sort_list[k] = rightHalf[j]
        j += 1
        k += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    global count
    count = 0
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        merge_sort(arr)

        fptr.write(str(count) + '\n')
        count = 0

    fptr.close()


# second and better one!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*
import math
import os
import random
import re
import sys

inv = 0


def merge(a, lena):
    # print('inv',inv)
    if (lena > 1):
        mid = lena // 2
        l = a[:mid]
        r = a[mid:]
        merge(l, mid)
        merge(r, lena - mid)
        i = j = k = 0
        # print('exec')
        global inv
        lenl = mid
        lenr = lena - mid
        while i < lenl and j < lenr:
            if (l[i] <= r[j]):
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
                inv += lenl - i
            k += 1
        while i < lenl:
            a[k] = l[i]
            i += 1
            k += 1

        while j < lenr:
            a[k] = r[j]
            j += 1
            k += 1
        # print(a)
    return (inv)


# Complete the countInversions function below.
def countInversions(arr):
    global inv
    inv = 0
    inversions = merge(arr, len(arr))
    return inversions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()










































