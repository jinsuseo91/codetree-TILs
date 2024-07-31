import copy

n, m, q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

wind = [list(map(int, input().split())) for _ in range(q)]

def in_range(x, y):
    if 0 <= x and x < n and 0 <= y and y < m:
        return True
    else: False

def change(r1, c1, r2, c2):
    u_row = arr[r1][c1:c2]
    d_row = arr[r2][c1+1:c2+1]

    r_col = [arr[r][c2] for r in range(r1, r2)]
    l_col = [arr[r][c1] for r in range(r1+1, r2+1)]
    
    u_row.insert(0, l_col[0])
    l_col.append(d_row[0])
    d_row.append(r_col[-1])
    r_col.insert(0, u_row[-1])

    u_row.pop(-1)
    r_col.pop(-1)
    d_row.pop(0)
    l_col.pop(0)

    arr[r1][c1:c2] = u_row
    arr[r2][c1+1:c2+1] = d_row

    for i in range(r1, r2):
        arr[i][c2] = r_col[i-r1]
    for i in range(r1+1, r2+1):
        arr[i][c1] = l_col[i-r1-1]
    return arr

def average(r1, c1, r2, c2, arr):
    result = copy.deepcopy(arr)
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            _sum = 0
            cnt = 1

            if in_range(i-1, j):
                _sum += arr[i-1][j]
                cnt += 1
            if in_range(i, j-1):
                _sum += arr[i][j-1]
                cnt += 1
            if in_range(i+1, j):
                _sum += arr[i+1][j]
                cnt += 1
            if in_range(i, j+1):
                _sum += arr[i][j+1]
                cnt += 1
            _sum += arr[i][j]
            

            result[i][j] = _sum//cnt

    return result

for i in wind:
    r1, c1, r2, c2 = i
    r1 -= 1
    r2 -= 1
    c1 -= 1
    c2 -= 1
    arr = change(r1, c1, r2, c2)
    arr = average(r1, c1, r2, c2, arr)
    

for i in range(n):
    for j in range(m):
        k = arr[i][j]
        print(k, end=' ')
    print()