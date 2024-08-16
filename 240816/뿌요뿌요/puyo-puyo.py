n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
visited = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or arr[x][y] != k:
        return False
    return True

def dfs(x, y, k):
    global cnt
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    visited[x][y] = 1
    cnt += 1

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y, k):
            dfs(new_x, new_y, k)

def get_block(k):
    global cnt, block

    for i in range(n):
        for j in range(n):
            if can_go(i, j, k):
                visited[i][j] == 1
                cnt = 0
                dfs(i, j, k)

                if cnt >= 4:
                    block += 1
                ans.append(cnt)
ans = []
block =0
for k in range(1, 101):
    get_block(k)
    visited = [[0] * n for _ in range(n)]
print(block, max(ans))