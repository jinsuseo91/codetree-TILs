R, C = map(int, input().split())

arr = [list(input().split()) for _ in range(R)]

x, y = 0, 0
c_color = arr[x][y]
cnt = 0
stop = 0
def in_range(i, j):
    return 0 <= i < R and 0 <= j < C

for i in range(R):
    for j in range(C):
        if in_range(i, j) and i >= x + 1 and j >= y + 1 and c_color != arr[i][j]:
            x, y = i, j
            c_color = arr[i][j]
            stop += 1
    if stop == 3 and (x, y) == (R-1, C-1):
        cnt += 1
print(cnt)