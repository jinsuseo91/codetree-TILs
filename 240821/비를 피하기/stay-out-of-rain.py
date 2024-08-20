from collections import deque

n, h, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and (arr[x][y] != 1)

def bfs():
    dxs, dys = [0, 1, 0, -1],[1, 0, -1, 0]
    while q:
        x, y, step = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                visited[nx][ny] = 1

                if arr[nx][ny] != 3:
                    q.append((nx, ny, step + 1))
                elif arr[nx][ny] == 3:
                    return step + 1
    return -1

def find_people_location():
    temp = []
    for i in range (n):
        for j in range (n):
            if arr[i][j] == 2:
                temp.append((i, j))
    return temp

people = find_people_location()

for p in people:
    x, y = p

    q = deque([(x, y, 0)])
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1

    result[x][y] = bfs()

for i in result:
    for j in i:
        print(j, end=' ')
    print()