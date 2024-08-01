import sys

n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

r, c = map(int, sys.stdin.readline().split())
r -= 1
c -= 1

boom = arr[r][c]

for i in range(boom):
    if r + i <= n:
        arr[r + i][c] = 0
    if r - i <= n:
        arr[r - i][c] = 0
    if c + i <= n:
        arr[r][c + i] = 0
    if c - i <= n:
        arr[r][c - i] = 0

for j in range(n):
    for i in range(n-1, 0, -1):
        if arr[i][j] == 0:
            arr[i][j] = arr[i-1][j]
            arr[i-1][j] = 0

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()