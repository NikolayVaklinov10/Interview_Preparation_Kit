def countSwaps(a):
    issorted = False
    swaps = 0

    while not issorted:
        issorted = True
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaps += 1
                issorted = False

    print("Array is sorted in %d swaps." % swaps)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[-1])










