

import os

a = ((19+3*33**(1/2))**(1/3) + (19-3*33**(1/2))**(1/3) + 1)/3
c = (a - 1)/(4*a - 6)

trib = lambda n: int(round(c * (a ** n)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = int(input())
    for s_itr in range(s):
        n = int(input())
        res = trib(n)
        fptr.write(str(res) + '\n')
    fptr.close()


# How it works:
#
# It is well known that fibonacci numbers can be calculated in
# O(log n) time using matrix exponentiation, similarly, tribonacci
# numbers can be found using: T = [[0, 1, 0], [0, 0, 1], [1, 1, 1]],
# the transformation matrix such that T*F_i = F_i+1 where F is [f(i-3),
# f(i-2), f(i-1)] The variable a in my solution is also known as the
# fibonacci constant, and is the only eigenvalue of T that is
# positive and real. (The other two eigenvalues have complex parts.)
#
# As shown in Dresden 2014
# (http://emis.ams.org/journals/JIS/VOL17/Dresden/dresden6.pdf),
# for 'large enough' values of n (in this case, n>=-1), you can
# throw away the terms depending on the complex eigenvalues,
# leaving us with this equation (after simplifying):
# F_n = rnd((a-1 / 4a-6) * a^n-1)
#
# A note on precision: The results returned here are only accurate
# up to n=52 because of the limitations of Python floats. This can
# be improved by using the built in Decimal class and setting a
# higher precision.
#
# And a note on speed: There are differences in **, pow, and math.pow
# for exponentiation. According to the answer here
# (https://stackoverflow.com/a/48848512), math.pow is O(1) time
# while ** and pow are O(log n), but some tests with timeit show
# that ** gives the best performance with small n values.


# cool one as well

seen = {0: 1}


def combine(n):
    if n < 0:
        return 0
    if n in seen:
        return seen[n]

    ret = combine(n - 1)
    ret += combine(n - 2)
    ret += combine(n - 3)
    seen[n] = ret
    return ret
