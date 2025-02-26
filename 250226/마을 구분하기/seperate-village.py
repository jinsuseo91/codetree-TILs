n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

peo = 0
ans = []
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
def can_go(x, y):
    return in_range(x, y) and arr[x][y] == 1 and visited[x][y] == False

def dfs(x, y):
    global peo
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True
            peo += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = True
            peo = 1
            dfs(i, j)
            ans.append(peo)

ans.sort()

print(len(ans))

for i in range(len(ans)):
    print(ans[i])