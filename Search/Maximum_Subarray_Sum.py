from bisect import insort, bisect_right

# solution 1
import bisect
def maximumSum(a, m):
    mm,pr=0,0
    a1=[]
    for i in a:
        pr=(pr+i)%m
        mm=max(mm,pr)
        ind=bisect.bisect_left(a1,pr+1)
        if(ind<len(a1)):
            mm=max(mm,pr-a1[ind]+m)
        bisect.insort(a1,pr)
    return mm


# solution 2

def maximumSum(a, m):
    # Create prefix tree
    prefix = [0] * len(a)
    curr = 0;
    for i in range(len(a)):
        curr = (a[i] % m + curr) % m
        prefix[i] = curr

    # Compute max modsum
    pq = [prefix[0]]
    maxmodsum = max(prefix)
    for i in range(1, len(a)):
        # Find cheapest prefix larger than prefix[i]
        left = bisect_right(pq, prefix[i])
        if left != len(pq):
            # Update maxmodsum if possible
            modsum = (prefix[i] - pq[left] + m) % m
            maxmodsum = max(maxmodsum, modsum)

        # add current prefix to heap
        insort(pq, prefix[i])

    return maxmodsum





