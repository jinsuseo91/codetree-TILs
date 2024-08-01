arr = [list(map(int, input().split())) for _ in range(4)]
n = 4
direction = input()

temp = [[0] * n for _ in range(n)]

Dir = {
    'D' : 0,
    'R' : 1,
    'U' : 2,
    'L' : 3
}

def rotate():
    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[n-1-j][i]
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]
            temp[i][j] = 0
    #print(arr)

def mul():
    drop()
    for j in range(n):
        for i in range(n-1, 0, -1):
            if not arr[i][j] or arr[i][j] != arr[i-1][j]:
                continue
            elif arr[i][j] == arr[i-1][j]:
                arr[i][j] *= 2
                arr[i-1][j] = 0
    drop()
    for _ in range(4 - Dir[direction]):
        rotate()

def drop():
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0
    for j in range(n):
        row = n-1
        for i in range(n-1, -1, -1):
            if arr[i][j] != 0:
                temp[row][j] = arr[i][j]
                row -= 1
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]

def rotate2(num):
    for i in range(num):
        rotate()
    mul()

rotate2(Dir[direction])

for i in range(n):
    for j in range(n):
        print(arr[i][j], end =' ')
    print()