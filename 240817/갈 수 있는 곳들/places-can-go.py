from collections import deque

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
start = []
q = deque()
cnt = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and arr[x][y] == 0 and not visited[x][y]

def bfs():
    global cnt
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))

for i in range(k):
    r, c = map(int, input().split())
    q.append((r - 1, c - 1))
    visited[r - 1][c - 1] = 1
    bfs()

for visit in visited:
    for v in visit:
        if v:
            cnt += 1

print(cnt)