from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1
visited = [[0] * n for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] 

def push(x, y, s):
    visited[x][y] = 1
    q.append((x, y, s))

def bfs():
    dxs, dys = [-1, -2, -2, -1, 1, 2, 2, 1], [2, 1, -1, -2, -2, -1, 1, 2]

    while q:
        x, y, step = q.popleft()
        if x == r2 and y == c2:
            return step

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny, step + 1)
    return step

push(r1, c1, 0)
ans = bfs()
if not visited[r2][c2]:
    print(-1)
else:
    print(ans)