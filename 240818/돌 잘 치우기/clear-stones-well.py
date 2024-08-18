from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
start = [list(map(int, input().split())) for _ in range(k)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, visited, grid):
    return in_range(x, y) and not visited[x][y] and not grid[x][y]

def bfs(grid):
    q = deque(start)
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[0] * n for _ in range(n)]
    for x, y in start:
        visited[x-1][y-1] = 1

    cnt = 1
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, visited, grid):
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt

# m개만큼 돌을 없앨 조합
all_1 = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            all_1.append([i, j])

one_list = list(combinations(all_1, m))
# 각 조합에 대해 돌을 치우고 bfs 실행
max_ = 0
for removed_ in one_list:
    arr_copy = [row[:] for row in arr]

    for x, y in removed_:
        arr_copy[x][y] = 0
    
    reach_ = bfs(arr_copy)

    max_ = max(max_, reach_)

print(max_)