# from collections import deque

# k, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(5)] #유물 그리드
# side_nums = list(map(int, input().split())) #벽면에 추가할 유물 종류들

# def rotate(temp,angle):
#     if angle == 90:
#         return [list(reversed(col)) for col in zip(*temp)]
#     elif angle == 180:
#         return [row[::-1] for row in temp[::-1]]
#     elif angle == 270:
#         return [list(col) for col in zip(*temp)][::-1]

# def rotate_grid(grid, r, c, angle):
#     #(r,c)를 좌상단으로 하는 3x3 서브 그리드를 시계방향으로 angle만큼 회전
#     temp = [row[c:c+3] for row in grid[r:r+3]] #기존 그리드를 안전하게 복사

#     rotated = rotate(temp, angle) #회전 결과 담을 그리드

#     new_grid = [row[:] for row in grid]
#     for i in range(3):
#         for j in range(3):
#             new_grid[r + i][c + j] = rotated[i][j]

#     return new_grid #회전된 그리드 반환

# def simulate(grid, copy_side):
#     #한 번의 회전 후 유물 제거 및 보충 시뮬레이션
#     #find_and_remove(grid)를 호출해서 유물 제거 및 가치 더하기
#     #refill_grid(grid, side_nums)를 호출해서 빈칸에 유물 추가
#     total_score = 0

#     while True:
#         removed, score = find_and_remove(grid)
#         total_score += score

#         if not removed:
#             break
#         refill_grid(grid, copy_side)

#     return total_score #유물 가치 반환

# def find_and_remove(grid):
#     #3개 이상의 연결된 유물 탐색(bfs), 제거, 점수 더하기
#     n = len(grid)
#     visited= [[False] * n for _ in range(n)]
#     removed = False
#     total_score = 0
#     dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

#     for i in range(n):
#         for j in range(n):
#             if grid[i][j] ==0 or visited[i][j]:
#                 continue

#             q = deque()
#             q.append((i, j))
#             visited[i][j] = True

#             same = [(i, j)] #같은거 3개 이상되는지
#             value = grid[i][j] #현재 유물 종류

#             while q:
#                 x, y = q.popleft()
#                 for dx, dy in zip(dxs, dys):
#                     nx, ny = x + dx, y + dy
#                     if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == value:
#                         visited[nx][ny] = True
#                         q.append((nx, ny))
#                         same.append((nx, ny))
            
#             if len(same) >= 3:
#                 removed = True
#                 total_score += len(same)
#                 for x, y in same:
#                     grid[x][y] = 0

#     return removed, total_score

# def refill_grid(grid, copy_side):
#     #0으로 된 칸에 벽면 유물을 우선 순위에 따라 삽입
#     #우선 순위 : 좌, 우, 하, 상
#     n = len(grid)

#     empty_cell = []
#     for i in range(n):
#         for j in range(n):
#             if grid[i][j] == 0:
#                 empty_cell.append((i, j))
    
#     empty_cell .sort(key=lambda x : (x[1],  -x[0]))

#     for x, y in empty_cell:
#         if copy_side:
#             grid[x][y] = copy_side.pop(0)
#         else:
#             break

# def get_all_rotation_options(grid, side_nums):
#     #모든 좌표랑 각도에 대해서 simulate 후 가장 높은 점수 찾기
#     #max()로 score에 대해서 최고점수 값 선택
#     n = len(grid)
#     best_score = -1
#     best_r, best_c, best_angle = -1, -1, -1

#     for r in range(n - 2):
#         for c in range(n - 2):
#             for angle in [90, 180, 270]:
#                 copy_grid = [row[:] for row in grid]
#                 rotated_grid = rotate_grid(copy_grid, r, c, angle)

#                 copy_side = side_nums[:]

#                 score = simulate(rotated_grid, copy_side)

#                 if score > best_score:
#                     best_score = score
#                     best_r, best_c, best_angle = r, c, angle

#     return best_r, best_c, best_angle, best_score

# result = []

# for _ in range(k):
#     total_score = 0

#     r, c, angle, _ = get_all_rotation_options(grid, side_nums)

#     grid = rotate_grid(grid, r, c, angle)

#     score = simulate(grid, side_nums)

#     total_score += score
#     if total_score != 0:
#         result.append(total_score)

# print(' '.join(map(str, result)))
from collections import deque

N = 5
N_SMALL = 3

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def rotate(grid, sy, sx, cnt):
    g = [row[:] for row in grid]
    for _ in range(cnt):
        temp = [[0]*N_SMALL for _ in range(N_SMALL)]
        for i in range(N_SMALL):
            for j in range(N_SMALL):
                temp[j][N_SMALL - 1 - i] = g[sy + i][sx + j]
        for i in range(N_SMALL):
            for j in range(N_SMALL):
                g[sy + i][sx + j] = temp[i][j]
    return g

def find_and_remove(grid):
    visited = [[False]*N for _ in range(N)]
    score = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or grid[i][j] == 0:
                continue
            q = deque()
            trace = []
            q.append((i, j))
            visited[i][j] = True
            trace.append((i, j))
            while q:
                y, x = q.popleft()
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if in_range(ny, nx) and not visited[ny][nx] and grid[ny][nx] == grid[y][x]:
                        visited[ny][nx] = True
                        q.append((ny, nx))
                        trace.append((ny, nx))
            if len(trace) >= 3:
                score += len(trace)
                for y, x in trace:
                    grid[y][x] = 0
    return score

def fill(grid, q):
    for j in range(N):
        for i in reversed(range(N)):
            if grid[i][j] == 0 and q:
                grid[i][j] = q.popleft()

def simulate(grid, side_nums):
    total_score = 0
    while True:
        fill(grid, side_nums)
        score = find_and_remove(grid)
        if score == 0:
            break
        total_score += score
    return total_score

def get_best_rotation(grid, side_nums):
    max_score = -1
    best_grid = None

    for cnt in range(1, 4):  # 90, 180, 270도 회전
        for sy in range(N - 2):
            for sx in range(N - 2):
                test_grid = rotate(grid, sy, sx, cnt)
                test_score_grid = [row[:] for row in test_grid]
                test_score = simulate(test_score_grid, deque(side_nums))  # simulate용 복사
                if test_score > max_score:
                    max_score = test_score
                    best_grid = rotate(grid, sy, sx, cnt)  # 실제 적용용 재회전

    return best_grid, max_score

# ===== 입력 =====
K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
side_nums = deque(map(int, input().split()))

# ===== 메인 루프 =====
result = []
for _ in range(K):
    best_grid, first_score = get_best_rotation(grid, side_nums)
    if first_score == 0 or best_grid is None:
        break
    grid = best_grid
    score = first_score + simulate(grid, side_nums)
    result.append(first_score)

# ===== 출력 =====
print(' '.join(map(str, result)))
