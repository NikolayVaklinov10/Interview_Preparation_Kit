
# solution 1
from collections import Counter


def checkMagazine(magazine, note):
    return (Counter(note) - Counter(magazine)) == {}
    # return not (Counter(ransom) - Counter(magazine)) OR THIS


# solution 2
from collections import defaultdict


def checkMagazine(magazine, note):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word] += 1
    for word in note:
        if dicty[word] == 0:
            return False
        dicty[word] -= 1
    return True


# solution 3
def checkMagazine(magazine, note):
    d = {}
    for word in magazine:
        d.setdefault(word, 0)
        d[word] += 1

    for word in note:
        if word in d:
            d[word] -= 1
        else:
            return False

    return all([x >= 0 for x in d.values()])


# solution 4
def checkMagazine(magazine, note):
  # sort both lists so we only have to loop once later
  magazine.sort()
  note.sort()
  i, j, matches = 0, 0, 0
  while i < len(note) and j < len(magazine):
    if note[i] == magazine[j]:
      matches += 1
      i += 1
    j += 1
    return True if matches == len(note) else False

#   SOLUTION !!!!!!!!!!!!!!!!!!!!!!!!!
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for i in note:
        try:
            del magazine[magazine.index(i)]
        except ValueError:
            print('No')
            return
    print('Yes')
    return


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)



