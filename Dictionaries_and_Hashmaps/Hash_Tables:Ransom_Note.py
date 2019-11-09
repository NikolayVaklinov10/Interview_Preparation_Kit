
# solution 1
from collections import Counter


def ransom_note(magazine, ransom):
    return (Counter(ransom) - Counter(magazine)) == {}


# solution 2
from collections import defaultdict


def ransom_note(magazine, ransom):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word] += 1
    for word in ransom:
        if dicty[word] == 0:
            return False
        dicty[word] -= 1
    return True










