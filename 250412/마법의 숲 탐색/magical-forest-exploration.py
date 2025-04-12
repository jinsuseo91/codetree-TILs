# R, C, K = map(int, input().split())
# unit = [list(map(int, input().split())) for _ in range(K)]
# arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]

# exit_set = set() #출구 좌표

# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]

# def bfs(si, sj):
#     q = []
#     visited = [[False] * (C + 2) for _ in range(R + 4)]
#     max_ = 0 #-2해서 return !! 쵀대 행값

#     q.append((si, sj))
#     visited[si][sj] = True

#     while q:
#         ci, cj = q.pop(0)
#         max_ = max(max_, ci)

#         for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             ni, nj = ci + dx, cj + dy
#             #방문하지 않았거나, 내 칸이거나, 현재 위치가 탈출구인데 다음칸이 골렘이라면
#             if not visited[ni][nj] and (arr[ci][cj] == arr[ni][nj] or ((ci, cj) in exit_set and arr[ni][nj] > 1)):
#                 q.append((ni, nj))
#                 visited[ni][nj] = True
#     return max_ - 2

# ans = 0
# num = 2
# for cj, dr in unit:
#     ci = 1
#     while True:
#         if arr[ci + 1][cj - 1] + arr[ci + 2][cj] + arr[ci + 1][cj + 1] == 0:
#             ci += 1
#         elif (arr[ci - 1][cj - 1] + arr[ci][cj - 2] + arr[ci + 1][cj - 1] + arr[ci + 1][cj - 2] + arr[ci + 2][cj - 1]) == 0:
#             ci += 1
#             cj -= 1
#             dr = (dr - 1) % 4
#         elif (arr[ci - 1][cj + 1] + arr[ci][cj + 2] + arr[ci + 1][cj + 1] + arr[ci + 1][cj + 2] + arr[ci + 2][cj + 1]) == 0:
#             ci += 1
#             cj += 1
#             dr = (dr + 1) % 4
#         else:
#             break

#     if ci < 4:
#         arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
#         exit_set = set()
#         num = 2

#     else: #골렘 표시, 탈출구 위치추가
#         arr[ci + 1][cj] = arr[ci - 1][cj] = num
#         arr[ci][cj - 1:cj + 2] = [num] * 3
#         num += 1

#         exit_set.add((ci + di[dr], cj + dj[dr]))

#         ans += bfs(ci, cj)

# print(ans)
from collections import deque

R, C, K = map(int, input().split())
unit = [list(map(int, input().split())) for i in range(K)]
arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
dxs, dys = [-1, 0 , 1, 0], [0, 1, 0,-1]
exit_set = set() #탈출구 정보 저장

def bfs(i, j):
    q = deque()
    visited = [[False] * (C + 2) for _ in range(R + 4)]
    max_ = 0
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        max_ = max(max_, x)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if not visited[nx][ny] and (arr[x][y] == arr[nx][ny] or ((x, y) in exit_set and arr[nx][ny] > 1)): #+탈출구인데 다음 칸이 골렘일 경우 가능
                q.append((nx, ny))
                visited[nx][ny] = True
    return max_ - 2

ans = 0  # 정답
num = 2  # 골렘번호
for j, d in unit:
    i = 1
    # 벽에 닿을 때 까지
    while True:
        # 남쪽으로
        if arr[i + 2][j] + arr[i + 1][j - 1] + arr[i + 1][j + 1] == 0:
            i += 1
        # 오른쪽아래로
        elif arr[i][j + 2] + arr[i - 1][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2] + arr[i + 2][j + 1] == 0:
            i += 1
            j += 1
            d = (d + 1) % 4
        # 왼쪽아래로
        elif arr[i][j - 2] + arr[i - 1][j - 1] + arr[i + 1][j - 1] + arr[i + 1][j - 2] + arr[i + 2][j - 1] == 0:
            i += 1
            j -= 1
            d = (d - 1) % 4
        # 더이상 갈 수없으면 종료
        else:
            break

    if i < 4:
        # 범위 안에 못들어오면 arr 초기화
        arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
        exit_set = set()
        num = 2
    else:
        # 같은 골렘 표시해주기
        arr[i + 1][j] = arr[i - 1][j] = num
        arr[i][j-1:j+2] = [num] * 3
        num += 1
        exit_set.add((i + dxs[d], j + dys[d]))
        ans += bfs(i, j)
print(ans)