n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# Please write your code here.
def init_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
zone = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    return in_range(x, y) and arr[x][y] > k and visited[x][y] == False

def dfs(x, y, k):
    visited[x][y] = True
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)

def get_zone(k):
    global zone
    zone = 0
    init_visited()
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = True
                zone += 1
                dfs(i, j, k)

max_ = -1
ans = 0
max_height = 101

for k in range(1, max_height):
    get_zone(k)
    if zone > max_:
        max_, ans = zone, k

print(ans, max_)