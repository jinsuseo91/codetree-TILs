from collections import deque
from itertools import combinations

n, k, u, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
coordinates = [(i, j) for i in range(n) for j in range(n)]

q = deque()

# 최대 도시 수
max_ = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, t, visited):
    return in_range(x, y) and u <= abs(arr[x][y] - t) <= d and not visited[x][y]

def bfs(city):
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for x, y in city:
        visited[x][y] = 1
        q.append((x, y))
        cnt += 1
    
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, arr[x][y], visited):
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt

for city in combinations(coordinates, k):
    max_ = max(max_, bfs(city))

print(max_)