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


