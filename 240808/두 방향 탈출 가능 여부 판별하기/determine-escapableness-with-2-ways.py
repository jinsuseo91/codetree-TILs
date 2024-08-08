n, m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global p
    dxs, dys = [1, 0], [0, 1]
    if x == n - 1 and y == m - 1:
        return 1

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y)
            visited[new_x][new_y] = False

visited[0][0] = True
dfs(0,0)
print(1 if dfs(0, 0) else 0)