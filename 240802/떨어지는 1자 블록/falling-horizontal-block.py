n, m, k = map(int, input().split())
k -= 1
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(i, j):
    return -1 <= i < n and 0 <= j < n

def can_move(x):
    for i in range(m):
        if arr[x + 1][k + i] == 1:
            return 0
        else:
            continue
    return 1

def simul():
    for i in range(-1, n-1):
        if can_move(i) == 0:
            break
        else:
            for j in range(k, k + m):
                if in_range(i, j):
                    arr[i + 1][j] = 1
                    if i > -1:
                        arr[i][j] = 0
                else:
                    break

simul()

for i in range(n):
    for j in range(n):
        print(arr[i][j], end =' ')
    print()