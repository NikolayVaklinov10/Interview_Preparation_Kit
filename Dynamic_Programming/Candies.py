def candies(n, arr):
    minArr1 = [1 for i in range(n)]
    minArr2 = [1 for i in range(n)]
    finalArr = []

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            minArr1[i]=minArr1[i-1]+1
        else:
            minArr1[i] = 1

    for j in range(len(arr)-2,-1,-1):
        if arr[j] > arr[j+1]:
            minArr2[j] = minArr2[j+1] +1
        else:
            minArr2[j] = 1

    for i in range(len(arr)):
        finalArr.append(max(minArr1[i], minArr2[i]))

    return sum(finalArr)