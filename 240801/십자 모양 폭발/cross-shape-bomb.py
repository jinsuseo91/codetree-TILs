import sys
BLANK = 0
n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
temp = [[0 for _ in range(n)] for _ in range(n)]

r, c = map(int, sys.stdin.readline().split())
r -= 1
c -= 1

boom = arr[r][c]

for i in range(boom):
    if 0 <= r + i < n:
        arr[r + i][c] = 0
    if 0 <= r - i < n:
        arr[r - i][c] = 0
    if 0 <= c + i < n:
        arr[r][c + i] = 0
    if 0 <= c - i < n:
        arr[r][c - i] = 0

for j in range(n):
    tempRow = n - 1
    for i in range(n-1, -1, -1):
        if arr[i][j] != 0:
            temp[tempRow][j] = arr[i][j]
            tempRow -= 1

for j in range(n):
    for i in range(n):
        arr[i][j] = temp[i][j]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()