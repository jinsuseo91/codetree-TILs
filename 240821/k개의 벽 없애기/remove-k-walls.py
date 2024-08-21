from collections import deque
from itertools import combinations

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

cnt = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, arr_copy, visited):
    return in_range(x, y) and not visited[x][y] and arr_copy[x][y] == 0

def bfs(arr_copy):
    q = deque([(r1, c1)])
    visited = [[0] * n for _ in range(n)]
    visited[r1][c1] = True
    step = [[0] * n for _ in range(n)]
    while q:
        x, y = q.popleft()
        if x == r2 and y == c2:
            return step[x][y]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny, arr_copy, visited):
                step[nx][ny] = step[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return -1

min_ = float('inf')
one_list = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            one_list.append((i, j))

for comb in combinations(one_list, k):
    arr_copy = [row[:] for row in arr]

    for x, y in comb:
        arr_copy[x][y] = 0
    
    reach_ = bfs(arr_copy)

    if reach_ != -1:
        min_ = min(reach_, min_)


print(min_ if min_ != float('inf') else -1)