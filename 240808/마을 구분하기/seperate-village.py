n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
# 마을 개수
cnt = 0
# 마을에 사는 사람들 정보
village = []

# 벽인 곳은 먼저 True로 만들어주기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            visited[i][j] = True

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global cnt
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    if arr[x][y] == 1:
        visited[x][y] = True
        arr[x][y] = 2
        cnt += 1

        # 네 방향 중에 1인 곳을 재호출
        for dx, dy in zip(dxs, dys) :
            new_x = x + dx
            new_y = y + dy
            if in_range(new_x, new_y) :
                dfs(new_x, new_y)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            a = dfs(i, j)
            if not a:
                village.append(cnt)
                cnt = 0
for i in range(len(village) * 2):
    if 0 in village:
        village.remove(0)
village.sort()
print(len(village))

for i in village:
    print(i)