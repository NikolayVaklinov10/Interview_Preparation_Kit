# solution 1
def get_median(counts, mids):
    res = []
    for mid in mids:
        gone = 0
        for i, v in enumerate(counts):
            gone += v
            if gone >= mid:
                res.append(i)
                break
    return sum(res) / len(res)


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    alerts = 0
    counts = [0] * 201

    if d % 2 == 1:
        mids = [d // 2 + 1]
    else:
        mids = [d // 2, d // 2 + 1]

    for v in expenditure[:d]:
        counts[v] += 1

    for i, exp in enumerate(expenditure[d:]):
        median = get_median(counts, mids)

        if exp >= 2 * median:
            alerts += 1

        old_value = expenditure[i]
        counts[old_value] -= 1
        counts[exp] += 1

    return alerts

# solution 2
def activityNotifications(expenditure, d):
    k = 200
    counter = 0

    count = (k + 1) * [0]  # indices runs from 0 to max(array) inclusive

    for i in expenditure[:d]:
        count[i] += 1  # Initial frequency array, jth value of count is the frequency of number j

    if (d % 2) == 1:  # Odd frequency case
        for i in range(d, len(expenditure)):
            cumfreq = (k + 1) * [0]
            cumfreq[0] = count[0]

            for j in range(1, k + 1):
                cumfreq[j] += cumfreq[j - 1] + count[j]

                if cumfreq[j] > (d) / 2:
                    median = j  # first j s.t. count[j-1] < (d+1)/2 and count[j] >= (d+1)/2
                    break
                else:
                    continue

            if expenditure[i] >= 2 * median:
                counter += 1

            count[expenditure[i - d]] -= 1
            count[expenditure[i]] += 1

    if (d % 2) == 0:  # Even frequency case
        for i in range(d, len(expenditure)):
            cumfreq = (k + 1) * [0]
            cumfreq[0] = count[0]

            m1 = None
            m2 = None

            for j in range(1, k + 1):
                cumfreq[j] += cumfreq[j - 1] + count[j]

                if (cumfreq[j] >= (d) / 2) and (m1 is None):
                    m1 = j

                if cumfreq[j] >= (d + 1) / 2:
                    m2 = j
                    median = (m1 + m2) / 2
                    break
                else:
                    continue

            if expenditure[i] >= 2 * median:
                counter += 1

            count[expenditure[i - d]] -= 1
            count[expenditure[i]] += 1

    return counter






######################################################################
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, d = map(int, input().split())
a = map(int, input().split())
noti = 0

# histogram for expenditure of the 1st d days
w = [0 ] *(201)
for i in range(d):
    w[a[i]] += 1

# calculate the median: index is the count of days till we get to the position of the median value
# in case of even sample size (d days), we need two values to calculate the median. To make it simpler, I separated the odd and the even case
for i in range( n -d):
    index, li, lo = 0, 0, 0
    if d% 2 != 0:
        for j in range(201):
            index += w[j]
            if index >= d / 2 + 1:
                med = float(j)
                break
    else:
        for j in range(201):
            index += w[j]
            if index >= (d / 2) and li == 0:
                li = j
            if index >= (d / 2 + 1) and lo == 0:
                lo = j
            if li != 0 and lo != 0:
                med = (float(li) + float(lo)) / 2
                break
    if float(a[d + i]) >= med * 2:
        noti += 1

        # move the window of d days forward by 1 day
    w[a[i]] -= 1
    w[a[d + i]] += 1

# we're done
print(noti)















