

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = abs(arr[0]-arr[len(arr)-1])
    for i in range(len(arr)-1):
        min_diff = min(abs(arr[i]-arr[i+1]), min_diff)
    return min_diff

