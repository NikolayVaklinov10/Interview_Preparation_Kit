# SOLUTION 1
from string import ascii_lowercase


def number_needed(a, b):
    count = 0
    for letter in ascii_lowercase:
        ia = a.count(letter)
        ib = b.count(letter)
        count += abs(ia - ib)
    return count


# SOLUTION 2

def number_needed(a,b):
    count = 0
    for i in range(97, 123):
        ia = sum(letter == chr(i) for letter in a)
        ib = sum(letter == chr(i) for letter in b)
        count += abs(ia-ib)
        return count

# solution 3
from math import fabs


def number_needed(a,b):
    letterArray = [0] * 26
    for c in a:
        index = ord(c) - ord('a')
        letterArray[index] += 1
    for c in b:
        index = ord(c) - ord('a')
        letterArray[index] -= 1
    result = 0
    for i in letterArray:
        result += fabs(i)
    return int(result)


a = input().strip()
b = input().strip()
print(number_needed(a,b))











