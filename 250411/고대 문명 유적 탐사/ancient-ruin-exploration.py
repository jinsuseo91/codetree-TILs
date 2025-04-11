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
from collections import deque

N_large = 5  # 고대 문명 전체 격자 크기입니다.
N_small = 3  # 회전시킬 격자의 크기입니다.

# 고대 문명 격자를 정의합니다
class Board:
    def __init__(self):
        self.a = [[0 for _ in range(N_large)] for _ in range(N_large)]

    def in_range(self, y, x):
        # 주어진 y, x가 고대 문명 격자의 범위안에 있는지 확인하는 함수 입니다.
        return 0 <= y < N_large and 0 <= x < N_large

    # 현재 격자에서 sy, sx를 좌측상단으로 하여 시계방향 90도 회전을 cnt번 시행했을때 결과를 return 합니다.
    def rotate(self, sy, sx, cnt):
        result = Board()
        result.a = [row[:] for row in self.a]
        for _ in range(cnt):
            # sy, sx를 좌측상단으로 하여 시계방향 90도 회전합니다.
            tmp = result.a[sy + 0][sx + 2]
            result.a[sy + 0][sx + 2] = result.a[sy + 0][sx + 0]
            result.a[sy + 0][sx + 0] = result.a[sy + 2][sx + 0]
            result.a[sy + 2][sx + 0] = result.a[sy + 2][sx + 2]
            result.a[sy + 2][sx + 2] = tmp
            tmp = result.a[sy + 1][sx + 2]
            result.a[sy + 1][sx + 2] = result.a[sy + 0][sx + 1]
            result.a[sy + 0][sx + 1] = result.a[sy + 1][sx + 0]
            result.a[sy + 1][sx + 0] = result.a[sy + 2][sx + 1]
            result.a[sy + 2][sx + 1] = tmp
        return result

    # 현재 격자에서 유물을 획득합니다.
    # 새로운 유물 조각을 채우는것은 여기서 고려하지 않습니다.
    def cal_score(self):
        score = 0
        visit = [[False for _ in range(N_large)] for _ in range(N_large)]
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

        for i in range(N_large):
            for j in range(N_large):
                if not visit[i][j]:
                    # BFS를 활용한 Flood Fill 알고리즘을 사용하여 visit 배열을 채웁니다.
                    # 이때 trace 안에 조각들의 위치가 저장됩니다.
                    q, trace = deque([(i, j)]), deque([(i, j)])
                    visit[i][j] = True
                    while q:
                        cur = q.popleft()
                        for k in range(4):
                            ny, nx = cur[0] + dy[k], cur[1] + dx[k]
                            if self.in_range(ny, nx) and self.a[ny][nx] == self.a[cur[0]][cur[1]] and not visit[ny][nx]:
                                q.append((ny, nx))
                                trace.append((ny, nx))
                                visit[ny][nx] = True
                    # 위에서 진행된 Flood Fill을 통해 조각들이 모여 유물이 되고 사라지는지 확인힙니다.
                    if len(trace) >= 3:
                        # 유물이 되어 사라지는 경우 가치를 더해주고 조각이 비어있음을 뜻하는 0으로 바꿔줍니다.
                        score += len(trace)
                        while trace:
                            t = trace.popleft()
                            self.a[t[0]][t[1]] = 0
        return score

    # 유물 획득과정에서 조각이 비어있는 곳에 새로운 조각을 채워줍니다.
    def fill(self, que):
        # 열이 작고 행이 큰 우선순위로 채워줍니다.
        for j in range(N_large):
            for i in reversed(range(N_large)):
                if self.a[i][j] == 0:
                    self.a[i][j] = que.popleft()

def main():
    # 입력을 받습니다.
    K, M = map(int, input().split())
    board = Board()
    for i in range(N_large):
        board.a[i] = list(map(int, input().split()))
    q = deque()
    for t in list(map(int, input().split())):
        q.append(t)

    # 최대 K번의 탐사과정을 거칩니다.
    for _ in range(K):
        maxScore = 0
        maxScoreBoard = None
        # 회전 목표에 맞는 결과를 maxScoreBoard에 저장합니다.
        # (1) 유물 1차 획득 가치를 최대화
        # (2) 회전한 각도가 가장 작은 방법을 선택
        # (3) 회전 중심 좌표의 열이 가장 작은 구간을, 그리고 열이 같다면 행이 가장 작은 구간을 선택
        for cnt in range(1, 4):
            for sx in range(N_large - N_small + 1):
                for sy in range(N_large - N_small + 1):
                    rotated = board.rotate(sy, sx, cnt)
                    score = rotated.cal_score()
                    if maxScore < score:
                        maxScore = score
                        maxScoreBoard = rotated
        # 회전을 통해 더 이상 유물을 획득할 수 없는 경우 탐사를 종료합니다.
        if maxScoreBoard is None:
            break
        board = maxScoreBoard
        # 유물의 연쇄 획득을 위해 유물 조각을 채우고 유물을 획득하는 과정을 더이상 획득할 수 있는 유물이 없을때까지 반복합니다.
        while True:
            board.fill(q)
            newScore = board.cal_score()
            if newScore == 0:
                break
            maxScore += newScore

        print(maxScore, end=" ")

if __name__ == '__main__':
    main()
