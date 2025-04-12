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
        for dx, dy in zip(dxs, dys):
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
        elif (arr[i][j - 2] + arr[i - 1][j - 1] + arr[i + 1][j - 1] + arr[i + 1][j - 2] + arr[i + 2][j - 1]) == 0:
            i += 1
            j -= 1
            d = (d - 1) % 4        
        elif (arr[i][j + 2] + arr[i - 1][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2] + arr[i + 2][j + 1]) == 0:
            i += 1
            j += 1
            d = (d + 1) % 4
        # 왼쪽아래로

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
        exit_set.add((i + dxs[d], j + dys[d]))
        num += 1
        ans += bfs(i, j)
print(ans)