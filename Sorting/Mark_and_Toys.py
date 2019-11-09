# solution 1
def maximumToys(prices, k):
    prices.sort()
    i = 0
    while k > 0 and i < len(prices):
        k -= prices[i]
        i += 1

    return i - 1


# solution 2
def maximumToys(prices, k):
    prices.sort()
    count = 0
    for i in prices:
        if i <= k:
            count += 1
            k -= i
        else:
            break
    return count














