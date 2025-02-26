n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(m)]
# Please write your code here.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and grid[x][y] == 1 and visited[x][y] == False

def dfs(x, y):
    visited[x][y] = True
    dxs, dys = [0, 1], [1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)
visited[0][0] = True
dfs(0, 0)
if visited[n-1][m-1] == True:
    print(1)
else:
    print(0)