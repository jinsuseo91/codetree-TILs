n, m, q = map(int, input().split())

ary = [list(map(int, input().split())) for _ in range(n)]

cost_l = []
direction_l = []

for _ in range(q):
    cost, direction = input().split()
    cost_l.append(int(cost))
    if direction == "L":
        direction = 0
    else:
        direction = 1
    direction_l.append(direction)

def up_check(x):
    if 0 <= x < n-1:
        for i in range(m):
            if ary[x][i] == ary[x+1][i]:
                return True
    return False

def down_check(x):
    if 0 <= x < n:
        for i in range(m):
            if ary[x][i] == ary[x-1][i]:
                return True
    return False

def change(ary, direction):
    if direction == 0:
        temp = ary[-1]
        for i in range(m-1, 0, -1):
            ary[i] = ary[i-1]
        ary[0] = temp
    else:
        temp = ary[0]
        for i in range(m-1):
            ary[i] = ary[i+1]
        ary[-1] = temp
    return ary
for x, direction in zip(cost_l, direction_l):
    x -= 1
    change(ary[x], direction)
    cnt = x - 1
    new_dir = direction + 1
    while cnt >= 0:
        if up_check(cnt):
            ary[cnt] = change(ary[cnt], new_dir % 2)
            cnt -= 1
            new_dir += 1
        else:
            break
    cnt = x + 1
    new_dir = direction + 1
    while cnt <= n-1:
        if down_check(cnt):
            ary[cnt] = change(ary[cnt], new_dir % 2)
            cnt += 1
            new_dir += 1
        else:
            break

for i in ary:
    for j in i:
        print(j, end=' ')
    print()