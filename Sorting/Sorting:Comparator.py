



# solution 1
def comparator(a, b):
    if a.score > b.score:
        return -1
    elif a.score < b.score:
        return 1
    elif a.score == b.score:
        if a.name > b.name:
            return 1
        elif a.name < b.name:
            return -1
        else:
            return 0

    def comparator(a, b):
        if a.score < b.score:
            return 1
        if a.score > b.score:
            return -1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0


# solution 2 improved
def cmp_to_key(key):
    return key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(self):
        return -self.score, self.name


