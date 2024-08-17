from collections import deque

NOT_EXISTS = (-1, -1)

n, k = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
r, c = map(int, input().split())
point = (r-1, c-1)
visited = [[0] * n for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, t):
    return in_range(x, y) and not visited[x][y] and arr[x][y] < t

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y = point
    visited[x][y] = 1
    q.append(point)
    t = arr[x][y]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny, t):
                visited[nx][ny] = 1
                q.append((nx, ny))

def need_update(best_pos, new_pos):
    if best_pos == NOT_EXISTS:
        return True
    
    best_x, best_y = best_pos
    nx, ny = new_pos
    
    return (arr[nx][ny], -nx, -ny) > (arr[best_x][best_y], -best_x, -best_y)

def move():
    global point
    initialize_visited()

    bfs()
    
    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            if not visited[i][j] or (i, j) == point:
                continue
            
            new_pos = (i, j)
            if need_update(best_pos, new_pos):
                best_pos = new_pos
    
    if best_pos == NOT_EXISTS:
        return False
    else:
        point = best_pos
        return True

for _ in range(k):
    if not move():
        break

fx, fy = point

print(fx + 1, fy + 1)