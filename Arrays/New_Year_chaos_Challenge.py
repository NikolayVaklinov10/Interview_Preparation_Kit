def minimumBribes(q):
    # Rearrange indexing since people are numbered 1...n but
    # indexing starts at 0
    q = [p - 1 for p in q]

    for spot, person in enumerate(q):
        # ex. if 3 is at 0th spot in line, 0 < 3 - 2, and this
        # person has moved up too far
        if spot < person - 2:
            print("Too chaotic")
            #return

    # anyone who overtook "person" has to be within the range of
    # one spot in front of "person"'s original position (and
    # one in front of "person"'s current position
    bribes = 0
    # no one overtook 0th person in line
    for spot, person in enumerate(q):
        # from one in front of original position to one
        # in front of current position
        for spot2 in range(max(person - 1, 0), spot):
            if q[spot2] > person:
                bribes += 1

    print(bribes)






























