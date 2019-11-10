
def getMinimumCost(n, k, c):
    cost = 0
    c = sorted(c, reverse=True)
    for i in range(0, n):
        cost += (i // k + 1) * c[i]
    return cost


# alternative to the above code for one liner
def getMinimumCost(k, c):
    return sum((v * (i // k + 1) for i, v in enumerate(sorted(c, reverse=True))))









