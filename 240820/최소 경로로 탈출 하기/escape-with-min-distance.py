from collections import deque

n ,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
step = [[-1] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and arr[x][y] == 1

def push(x, y ,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

push(0, 0, 0)
bfs()

print(step[n-1][m-1])