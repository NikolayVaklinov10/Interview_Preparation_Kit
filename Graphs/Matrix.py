from disjoint_set import DisjointSet
import ddict


def minTime(roads, machines):
    parent = {}
    dp = ddict(int)  #dp[i] denotes whether or not component with root i had already had a machine
    for machine in machines : dp[machine] = 1
    find = lambda node : node if parent.get(node, node) == node else find(parent[node])
    def union(i,j):
        x,y = find(i), find(j)
        if not dp[x] or not dp[y]:
            if i != x : x,y = y,x
            parent[x] = y
            dp[x] |= dp[y]
            dp[y] |= dp[x]
            return True
    return sum(time for i,j, time in sorted(roads, key = lambda i : -i[2]) if not union(i,j))