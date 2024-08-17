from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and arr[x][y] == 1 and visited[x][y] == 0

def bfs():
    dxs, dys = [1, 0, -1], [0, 1, 0]
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

visited[0][0] = 1
q.append((0, 0))
bfs()
print(visited[n-1][m-1])