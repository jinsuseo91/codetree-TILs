n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
#points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from collections import deque
q = deque()
cnt = 0 #방문 가능 칸

visited = [[False] * n for _ in range(n)]
points = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and grid[x][y] == 0 and not visited[x][y]

def bfs():
    while q:
        x, y = q.popleft()
        dxs, dys = [0, 1, 0 ,-1], [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

for _ in range(k):
    x, y = map(int, input().split())
    q.append((x - 1, y - 1))
    visited[x - 1][y - 1] = True

bfs()

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            cnt += 1

print(cnt)