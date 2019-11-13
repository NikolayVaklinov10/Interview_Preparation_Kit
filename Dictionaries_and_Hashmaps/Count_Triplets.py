from collections import defaultdict


def countTriplets(arr, r):
    counter={a: 0 for a in arr}
    tuplets={a: 0 for a in arr}
    triplets=0
    for a in arr[::-1]:
        try:
            triplets+=tuplets[r*a]
            tuplets[a]+=counter[r*a]
        except:
            None
        counter[a]+=1
    return triplets

# TODO: use defaultdict(int) instead
#  of try/catch block + initialization
#  for counter and tuplets variables


def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

    return count
