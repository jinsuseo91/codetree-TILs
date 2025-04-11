# from collections import deque

# k, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(5)] #유물 그리드
# q = deque()
# for t in list(map(int, input().split())):
#     q.append(t)

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

# N_large = 5  # 고대 문명 전체 격자 크기입니다.
# N_small = 3  # 회전시킬 격자의 크기입니다.

# for _ in range(k):

#     total_score = 0

#     r, c, angle, _ = get_all_rotation_options(grid, side_nums)

#     grid = rotate_grid(grid, r, c, angle)

#     score = simulate(grid, side_nums)

#     total_score += score
#     if total_score != 0:
#         result.append(total_score)

# print(' '.join(map(str, result)))

# import pprint
# import collections

# K, M = [int(x) for x in input().split()]
# board = []
# dx, dy = [1,0,-1,0], [0,1,0,-1]
# answer = []

# for _ in range(5):
#     board.append([int(x) for x in input().split()])

# walls = [int(x) for x in input().split()]
# wall_idx = 0

# def OOB(x, y):
#     return x<0 or x>=5 or y<0 or y>=5

# def rotate(x, y): 
#     x, y = (x-1), (y-1)
#     tmp_board = [[0] * 3 for _ in range(3)]
#     for i in range(3):
#         for j in range(3):
#             tmp_board[i][j] = board[x+2-j][y+i]

#     for i in range(3):
#         for j in range(3):
#             board[x+i][y+j] = tmp_board[i][j]

# def bfs():

#     queue = collections.deque([])
#     vis = collections.defaultdict(int)
#     paths = collections.defaultdict(list)
#     treasures = set()

#     for i in range(5):
#         for j in range(5):
#             if vis[(i, j)]: continue
#             vis[(i, j)] = 1
#             queue.append(((i, j), (i, j)))
            
#             while queue :
#                 (x, y), (px, py) = queue.popleft()
#                 paths[(px, py)].append((x, y))
                
#                 is_last = 1
#                 for dir in range(4):
#                     nx, ny = x+dx[dir], y+dy[dir]
#                     if OOB(nx, ny) or vis[(nx, ny)] or board[x][y] != board[nx][ny]:
#                         continue
#                     is_last = 0
#                     vis[(nx, ny)] = 1
#                     queue.append(((nx, ny), (px, py)))
                
#                 if is_last and len(paths[(px, py)]) >= 3 :
#                     for cur in paths[(px, py)] :
#                         treasures.add(cur)
    
#     return list(treasures)



# r, c, d, treasures = 5, 5, 4, []
# while K :
#     for i in range(1, 4):
#         for j in range(1, 4):
#             for new_d in range(3):
#                 rotate(i, j)
#                 new_treasures = bfs()
#                 if [len(treasures), -d, -c, -r] < [len(new_treasures), -new_d, -j, -i] :
#                     r, c, d = i ,j, new_d
#                     treasures = new_treasures
#             rotate(i, j)

    
#     if len(treasures) == 0 :
#         break
#     else :
#         for _ in range(d+1):
#             rotate(r, c)

#     tmp_sum = 0
#     while treasures : 
#         tmp_sum += len(treasures)
#         treasures.sort(key= lambda x: (x[1], -x[0])) 
#         for (x, y) in treasures :
#             board[x][y] = walls[wall_idx]
#             wall_idx = (wall_idx + 1) % M
#         treasures = bfs()

#     answer.append(tmp_sum)
#     K -= 1

# print(*answer)

from collections import deque

N = 5
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def rotate(temp, angle):
    if angle == 90:
        return [list(reversed(col)) for col in zip(*temp)]
    elif angle == 180:
        return [row[::-1] for row in temp[::-1]]
    elif angle == 270:
        return [list(col) for col in zip(*temp)][::-1]

def rotate_grid(grid, x, y, angle):
    temp = [row[y:y+3] for row in grid[x:x+3]]
    rotated = rotate(temp, angle)
    new_grid = [row[:] for row in grid]
    for i in range(3):
        for j in range(3):
            new_grid[x+i][y+j] = rotated[i][j]
    return new_grid

def find_artifacts(grid):
    visited = [[False] * N for _ in range(N)]
    found = set()
    for i in range(N):
        for j in range(N):
            if visited[i][j] or grid[i][j] == 0:
                continue
            q = deque()
            group = []
            q.append((i, j))
            group.append((i, j))
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        group.append((nx, ny))
            if len(group) >= 3:
                found.update(group)
    return list(found)

def refill_grid(grid, artifacts, walls, wall_idx):
    artifacts.sort(key=lambda x: (x[1], -x[0]))  # 열 오름차순, 행 내림차순
    for x, y in artifacts:
        grid[x][y] = walls[wall_idx % len(walls)]
        wall_idx += 1
    return wall_idx

# ✅ 입력
K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
walls = list(map(int, input().split()))

wall_idx = 0
result = []

while K:
    best_score = -1
    best_grid = None
    best_angle = best_x = best_y = 999
    best_artifacts = []

    for x in range(N - 2):
        for y in range(N - 2):
            for angle in [90, 180, 270]:
                rotated = rotate_grid(grid, x, y, angle)
                artifacts = find_artifacts(rotated)
                score = len(artifacts)
                if (score > best_score or
                    (score == best_score and angle < best_angle) or
                    (score == best_score and angle == best_angle and y < best_y) or
                    (score == best_score and angle == best_angle and y == best_y and x < best_x)):
                    best_score = score
                    best_grid = rotate_grid(grid, x, y, angle)
                    best_angle, best_x, best_y = angle, x, y
                    best_artifacts = artifacts

    if best_score == 0:
        break

    grid = best_grid
    total = 0

    while True:
        total += len(best_artifacts)
        wall_idx = refill_grid(grid, best_artifacts, walls, wall_idx)
        best_artifacts = find_artifacts(grid)
        if not best_artifacts:
            break

    result.append(total)
    K -= 1

print(*result)
