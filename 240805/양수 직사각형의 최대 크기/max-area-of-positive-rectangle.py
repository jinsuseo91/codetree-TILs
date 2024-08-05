n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

max_size = -1

# 모든 직사각형을 확인하고 모든 값이 양수인 직사각형만 리턴
def can_rect(x1, y1, x2, y2):
    return all([
        arr[i][j] > 0
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if can_rect(i, j, k, l):
                    max_size = max(max_size, (k - i + 1) * (l - j + 1))


print(max_size)