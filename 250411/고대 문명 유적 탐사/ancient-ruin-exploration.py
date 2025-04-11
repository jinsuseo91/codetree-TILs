from collections import deque

k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)] #유물 그리드
side_nums = list(map(int, input().split())) #벽면에 추가할 유물 종류들

def rotate(temp,angle):
    if angle == 90:
        return [list(reversed(col)) for col in zip(*temp)]
    elif angle == 180:
        return [row[::-1] for row in temp[::-1]]
    elif angle == 270:
        return [list(col) for col in zip(*temp)][::-1]

def rotate_grid(grid, r, c, angle):
    #(r,c)를 좌상단으로 하는 3x3 서브 그리드를 시계방향으로 angle만큼 회전
    temp = [row[c:c+3] for row in grid[r:r+3]] #기존 그리드를 안전하게 복사

    rotated = rotate(temp, angle) #회전 결과 담을 그리드

    new_grid = [row[:] for row in grid]
    for i in range(3):
        for j in range(3):
            new_grid[r + i][c + j] = rotated[i][j]

    return new_grid #회전된 그리드 반환

def simulate(grid, copy_side):
    #한 번의 회전 후 유물 제거 및 보충 시뮬레이션
    #find_and_remove(grid)를 호출해서 유물 제거 및 가치 더하기
    #refill_grid(grid, side_nums)를 호출해서 빈칸에 유물 추가
    total_score = 0

    while True:
        removed, score = find_and_remove(grid)
        total_score += score

        if not removed:
            break
        refill_grid(grid, copy_side)

    return total_score #유물 가치 반환

def find_and_remove(grid):
    #3개 이상의 연결된 유물 탐색(bfs), 제거, 점수 더하기
    n = len(grid)
    visited= [[False] * n for _ in range(n)]
    removed = False
    total_score = 0
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            if grid[i][j] ==0 or visited[i][j]:
                continue

            q = deque()
            q.append((i, j))
            visited[i][j] = True

            same = [(i, j)] #같은거 3개 이상되는지
            value = grid[i][j] #현재 유물 종류

            while q:
                x, y = q.popleft()
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == value:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        same.append((nx, ny))
            
            if len(same) >= 3:
                removed = True
                total_score += len(same)
                for x, y in same:
                    grid[x][y] = 0

    return removed, total_score

def refill_grid(grid, copy_side):
    #0으로 된 칸에 벽면 유물을 우선 순위에 따라 삽입
    #우선 순위 : 좌, 우, 하, 상
    n = len(grid)

    empty_cell = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                empty_cell.append((i, j))
    
    empty_cell .sort(key=lambda x : (x[1],  -x[0]))

    for x, y in empty_cell:
        if copy_side:
            grid[x][y] = copy_side.pop(0)
        else:
            break

def get_all_rotation_options(grid, side_nums):
    #모든 좌표랑 각도에 대해서 simulate 후 가장 높은 점수 찾기
    #max()로 score에 대해서 최고점수 값 선택
    n = len(grid)
    best_score = -1
    best_r, best_c, best_angle = -1, -1, -1

    for r in range(n - 2):
        for c in range(n - 2):
            for angle in [90, 180, 270]:
                copy_grid = [row[:] for row in grid]
                rotated_grid = rotate_grid(copy_grid, r, c, angle)

                copy_side = side_nums[:]

                score = simulate(rotated_grid, copy_side)

                if score > best_score:
                    best_score = score
                    best_r, best_c, best_angle = r, c, angle

    return best_r, best_c, best_angle, best_score

result = []

for _ in range(k):
    total_score = 0

    r, c, angle, _ = get_all_rotation_options(grid, side_nums)

    grid = rotate_grid(grid, r, c, angle)

    score = simulate(grid, side_nums)

    total_score += score
    if total_score != 0:
        result.append(total_score)

print(' '.join(map(str, result)))