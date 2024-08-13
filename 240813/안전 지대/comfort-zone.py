import sys
sys.setrecursionlimit(10000)

# 입력 받기
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y, k):
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cur_x, cur_y = stack.pop()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = cur_x + dx, cur_y + dy
            if in_range(new_x, new_y) and not visited[new_x][new_y] and arr[new_x][new_y] > k:
                visited[new_x][new_y] = True
                stack.append((new_x, new_y))

max_k = max(max(row) for row in arr)
best_k = 1
max_safe_zones = 0

# K 값을 1부터 최대 K까지 변화시키면서 시뮬레이션
for k in range(1, max_k + 1):
    visited = [[False] * m for _ in range(n)]
    safe_zone_count = 0
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] > k and not visited[i][j]:
                dfs(i, j, k)
                safe_zone_count += 1
    
    # 최대 안전 지대 수를 찾고, 해당하는 K를 기록
    if safe_zone_count > max_safe_zones:
        max_safe_zones = safe_zone_count
        best_k = k

# 결과 출력
print(best_k, max_safe_zones)