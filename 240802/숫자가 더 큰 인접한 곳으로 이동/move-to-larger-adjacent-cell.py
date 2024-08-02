n, r, c = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(n)]
result = []
def in_range(x,y):
    return 0 <= x < n and 0 <= y < n
def simul():
    global r, c
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    a= 0
    next_num = 0
    next_pos = (-1,-1)
    curr_pos = next_pos

    for dx, dy in zip(dxs, dys):
        next_x, next_y = r + dx, c + dy
        if in_range(next_x, next_y) and arr[next_x][next_y] > arr[r][c]:
            if a != 1:
                next_num = arr[next_x][next_y]
                next_pos = (next_x, next_y)
                print(next_num, end =' ')
                r, c = next_pos
                a = 1
        else:
             continue
    if a == 1:
        return 1
    else:
        return 0
        
print(arr[r][c], end=' ')
while True:
    if simul() == 0:
        break
    else:
        simul()