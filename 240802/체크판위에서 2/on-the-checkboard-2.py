n, m = map(int, input().split())

arr = [list(input().split()) for _ in range(n)]

cnt = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(i + 1, n - 1):
            for l in range(j + 1, m - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다.
                if arr[0][0] != arr[i][j] and arr[i][j] != arr[k][l] and arr[k][l] != arr[n - 1][m - 1]:
                    cnt += 1
print(cnt)