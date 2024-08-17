from collections import deque

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or arr[x][y] == 0:
        return False
    return True

def bfs():
    dxs, dys = [1, 0, -1], [0, 1, 0]
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append([nx, ny])
    #         if nx == n - 1 and ny == m - 1:
    #             check = 1
    #             return check
    #         else:
    #             check = 0
    # return check

q.append((0, 0))
visited[0][0] = 1
result = bfs()
print(visited[n-1][m-1])