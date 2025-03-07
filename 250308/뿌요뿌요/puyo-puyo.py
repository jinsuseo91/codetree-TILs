n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

max_block, bomb_cnt = 0, 0
curr_block_num = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, num):
    return in_range(x, y) and visited[x][y] == False and grid[x][y] == num

def dfs(x, y):
    global curr_block_num
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, grid[x][y]):
            visited[nx][ny] = True
            curr_block_num += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            visited[i][j] = True
            curr_block_num = 1
            dfs(i, j)

            if curr_block_num >= 4:
                bomb_cnt += 1
            max_block = max(max_block, curr_block_num)

print(bomb_cnt, max_block)