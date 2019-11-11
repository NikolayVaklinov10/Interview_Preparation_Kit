from collections import deque


def minimumMoves(grid, startY, startX, goalY, goalX):
    q = deque()
    q.append((startX, startY, 0, -1))
    visited = {(startY, startX): 0}
    x, y = [-1, 0, 0, 1, 1], [0, 1, -1, 0, 1]
    def is_valid(x, y, new_dist):
        return x < len(grid) and y < len(grid) and x >= 0 and y >= 0 and grid[y][x] == '.' and ((y, x) not in visited or ((y, x) in visited and new_dist <= visited[(y, x)]))
    while q:
        n = q.pop()
        for k in range(4):
            dist = 0 if (x[k], y[k]) == (x[n[3]], y[n[3]]) else 1
            if is_valid(n[0] + x[k], n[1] + y[k], n[2] + dist):
                visited[(n[1] + y[k], n[0] + x[k])] = n[2] + dist
                q.appendleft((n[0] + x[k], n[1] + y[k], n[2] + dist, k))
    return visited[(goalY ,goalX)]










