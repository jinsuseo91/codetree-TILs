n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

def is_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n 


def get_score(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_num = [k,l,k,l]
    m_sum = 0
    for dx, dy, move_num in zip(dxs, dys, move_num):
        for _ in range(move_num):
            x = x + dx
            y = y + dy

            if not is_range(x,y):
                return 0
            
            m_sum += array[x][y]
    return m_sum
max_sum = 0
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                max_sum = max(max_sum, get_score(i,j,k,l))
print(max_sum)