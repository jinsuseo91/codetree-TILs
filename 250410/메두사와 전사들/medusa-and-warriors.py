from collections import deque
import sys
INF = int(1e9) + 10
input = sys.stdin.read
data = input().split()
idx = 0

n = int(data[idx]); idx += 1  # 그리드 크기 N
m = int(data[idx]); idx += 1  # 전사 수 M

start_x = int(data[idx]); idx += 1
start_y = int(data[idx]); idx += 1
end_x = int(data[idx]); idx += 1
end_y = int(data[idx]); idx += 1

# 초기 전사 위치 입력
warrior_position = []
for _ in range(m):
    x = int(data[idx]); idx += 1
    y = int(data[idx]); idx += 1
    warrior_position.append((x, y))

# 장애물 그리드 입력
obstacle_grid = []
for _ in range(n):
    row = []
    for _ in range(n):
        cell = int(data[idx]); idx += 1
        row.append(cell)
    obstacle_grid.append(row)

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] #상하좌우 순서

def cal_distance(a, b): #전사가 메두사한테 접근할 때 어디로 이동해야하는지 판단하려고 사용
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(x, y, n, obstacle_grid): #메두사의 최단거리
    distance_grid = [[INF if obstacle_grid[i][j] else -1 for j in range(n)] for i in range(n)]

    q = deque()
    q.append((x, y))
    distance_grid[x][y] = 0

    while q:
        current_x, current_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < n and 0 <= ny <n and distance_grid[nx][ny] == -1:
                distance_grid[nx][ny] = distance_grid[current_x][current_y] + 1
                q.append((nx, ny))

    return distance_grid

def sight_up(x, y, n, is_test, warrior_count_grid, sight_map):
    '''
    x, y : 현재 메두사 위치
    n : 그리드 크기
    is_test : 테스트 모드인지 여부
    warrior_count_grid : 각 셀에 있는 전사의 수
    sight_map : 현재 시야 상태
    return : 시야로 커버된 전사의 수
    '''
    for i in range(x - 1, -1, -1):
        left = max(0, y - (x - i))
        right = min(n - 1, y + (x - i))
        for j in range(left, right + 1):
            sight_map[i][j] = 1 #보이는 곳을 1로 설정

    #장애물 처리
    obstruction_found = False
    for i in range(x - 1, -1, -1):
        if obstruction_found: #장애물이 있으면
            sight_map[i][y] = 0
        else:
            sight_map[i][y] = 1

        if warrior_count_grid[i][y]:
            obstruction_found = True

    for i in range(x - 1, 0, -1):
        left = max(0, y - (x - i))
        right = min(n - 1, y + (x - i))

        for j in range(left, y): #왼쪽 시야 정리
            if not sight_map[i][j] or warrior_count_grid[i][j]:
                if j > 0:
                    sight_map[i - 1][j - 1] = 0 #왼쪽 위 시야 제거
                sight_map[i - 1][j] = 0 #바로 위 시야 제거

        for j in range(y + 1, right + 1):
            if not sight_map[i][j] or warrior_count_grid[i][j]:
                if j + 1 < n:
                    sight_map[i - 1][j + 1] = 0
                sight_map[i - 1][j] = 0

    coverage = 0 #시야에 보이는 전사의 수
    for i in range(x - 1, -1, -1):
        left = max(0, y - (x - i))
        right = min(n - 1, y + (x - i))
        for j in range(left, right + 1):
            if sight_map[i][j]: #시야가 보이는곳
                coverage += warrior_count_grid[i][j]

    if is_test:
        for i in range(x - 1, -1, -1):
            left = max(0, y - (x - i))
            right = min(n - 1, y + (x - i))
            for j in range(left, right + 1):
                sight_map[i][j] = 0
    
    return coverage

def sight_down(x, y, n, is_test, warrior_count_grid, sight_map):
    for i in range(x + 1, n):
        left = max(0, y - (i - x))
        right = min(n - 1, y + (i - x))
        for j in range(left, right + 1):
            sight_map[i][j] = 1

    obstruction_found = False
    for i in range(x + 1, n):
        if obstruction_found:
            sight_map[i][y] = 0
        else:
            sight_map[i][y] = 1

        if warrior_count_grid[i][y]:
            obstruction_found = True

    for i in range(x + 1, n - 1):
        left = max(0, y - (i - x))
        right = min(n - 1, y + (i - x))

        for j in range(left, y):
            if not sight_map[i][j] or warrior_count_grid[i][j]:
                if j > 0:
                    sight_map[i + 1][j - 1] = 0
                sight_map[i + 1][j] = 0

        for j in range(y, right + 1):
            if not sight_map[i][j] or warrior_count_grid[i][j]:
                if j < n - 1:
                    sight_map[i + 1][j + 1] = 0
                sight_map[i + 1][j] = 0

    coverage = 0
    for i in range(x + 1, n):
        left = max(0, y - (i - x))
        right = min(n - 1, y + (i - x))

        for j in range(left, right + 1):
            if sight_map[i][j]:
                coverage += warrior_count_grid[i][j]

    if is_test:
        for i in range(x + 1, n):
            left = max(0, y - (i - x))
            right = min(n - 1, y + (i - x))
            for j in range(left, right + 1):
                sight_map[i][j] = 0

    return coverage

def sight_left(x, y, n, is_test, warrior_count_grid, sight_map):
    for i in range(y - 1, -1, -1):
        top = max(0, x - (y - i))
        bottom = min(n - 1, x + (y - i))
        for j in range(top, bottom + 1):
            sight_map[j][i] = 1

    obstruction_found = False
    for i in range(y - 1, -1, -1):
        if obstruction_found:
            sight_map[x][i] = 0
        else:
            sight_map[x][i] = 1

        if warrior_count_grid[x][i]:
            obstruction_found = True
    
    for i in range(y - 1, 0, -1):
        top = max(0, x - (y - i))
        bottom = min(n - 1, x + (y - i))

        for j in range(top, x):
            if not sight_map[j][i] or warrior_count_grid[j][i]:
                if j > 0:
                    sight_map[j - 1][i - 1] = 0
                sight_map[j][i - 1] = 0

        for j in range(x + 1, bottom + 1):
            if not sight_map[j][i] or warrior_count_grid[j][i]:
                if j < n - 1:
                    sight_map[j + 1][i - 1] = 0
                sight_map[j][i - 1] = 0

    coverage = 0
    for i in range(y - 1, -1, -1):
        top = max(0, x - (y - i))
        bottom = min(n - 1, x + (y - i))
        for j in range(top, bottom + 1):
            if sight_map[j][i]:
                coverage += warrior_count_grid[j][i]

    if is_test:
        for i in range(y - 1, -1, -1):
            top = max(0, x - (y - i))
            bottom = min(n - 1, x + (y - i))
            for j in range(top, bottom + 1):
                sight_map[j][i] = 0
    return coverage

def sight_right(x, y, n, is_test, warrior_count_grid, sight_map):

    for i in range(y + 1, n):
        top = max(0, x - (i - y))
        bottom = min(n - 1, x + (i - y))
        for j in range(top, bottom + 1):
            sight_map[j][i] = 1  # 시야 설정

    # 장애물 처리: 시야 막힘 여부 확인
    obstruction_found = False
    for i in range(y + 1, n):
        if obstruction_found:
            sight_map[x][i] = 0  # 장애물이 발견된 후에는 시야 제거
        else:
            sight_map[x][i] = 1  # 장애물이 발견되지 않으면 시야 유지

        if warrior_count_grid[x][i]:
            obstruction_found = True  # 전사가 있는 경우 장애물로 간주

    # 장애물에 따라 시야 조정
    for i in range(y + 1, n - 1):
        top = max(0, x - (i - y))
        bottom = min(n - 1, x + (i - y))

        # 상단 측면 조정
        for j in range(top, x):
            if not sight_map[j][i] or warrior_count_grid[j][i]:
                if j > 0:
                    sight_map[j - 1][i + 1] = 0  # 오른쪽 위 셀의 시야 제거
                sight_map[j][i + 1] = 0          # 바로 오른쪽 셀의 시야 제거

        # 하단 측면 조정
        for j in range(x + 1, bottom + 1):
            if not sight_map[j][i] or warrior_count_grid[j][i]:
                if j + 1 < n and i + 1 < n:
                    sight_map[j + 1][i + 1] = 0  # 오른쪽 아래 셀의 시야 제거
                sight_map[j][i + 1] = 0          # 바로 오른쪽 셀의 시야 제거

    # 시야로 커버된 전사 수 계산
    coverage = 0
    for i in range(y + 1, n):
        top = max(0, x - (i - y))
        bottom = min(n - 1, x + (i - y))
        for j in range(top, bottom + 1):
            if sight_map[j][i]:
                coverage += warrior_count_grid[j][i]

    # 테스트 모드인 경우 시야 맵을 원래대로 되돌림
    if is_test:
        for i in range(y + 1, n):
            top = max(0, x - (i - y))
            bottom = min(n - 1, x + (i - y))
            for j in range(top, bottom + 1):
                sight_map[j][i] = 0  # 시야 제거

    return coverage

def choose_best_sight(x, y, n, warrior_count_grid, sight_map):
    for i in range(n):
        for j in range(n):
            sight_map[i][j] = 0

    max_coverage = -1
    best_direction = -1

    sight_function = [sight_up, sight_down, sight_left, sight_right]

    for dir in range(4):
        for i in range(n):
            for j in range(n):
                sight_map[i][j] = 0

        coverage = sight_function[dir](x, y, n, True, warrior_count_grid, sight_map)
        if max_coverage < coverage:
            max_coverage = coverage
            best_direction = dir

    assert best_direction != -1, '최적의 시야 방향을 찾을 수 없습니다.'

    sight_function[best_direction](x, y, n,False, warrior_count_grid, sight_map)

    return max_coverage

def move_warriors(player_x, player_y, n, m, warrior_position, sight_map):
    total_moved = 0
    total_hits = 0

    move_dx = [-1, 1, 0, 0]
    move_dy = [0, 0, -1, 1]

    for i in range(m):
        if warrior_position[i][0] == -1:
            continue

        warrior_x, warrior_y = warrior_position[i]

        if sight_map[warrior_x][warrior_y]: #시야에 있는 전사는 이동X
            continue

        current_distance = cal_distance((player_x, player_y), (warrior_x, warrior_y))
        has_moved = False

        for dir in range(4):
            nx = warrior_x + move_dx[dir]
            ny = warrior_y + move_dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
            if sight_map[nx][ny]:
                    continue
                    
            new_distance = cal_distance((player_x, player_y), (nx, ny))
            
            if new_distance < current_distance:
                warrior_x, warrior_y = nx, ny
                has_moved = True
                total_moved += 1
                break

        if has_moved:
            new_distance = cal_distance((player_x, player_y), (warrior_x, warrior_y))
            for dir in range(4):
                opposite_dir = (dir + 2) % 4
                nx = warrior_x + move_dx[opposite_dir]
                ny = warrior_y + move_dy[opposite_dir]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if sight_map[nx][ny]:
                    continue

                # 새로운 위치에서의 거리 계산
                further_distance = cal_distance((player_x, player_y), (nx, ny))
                if further_distance < new_distance:
                    warrior_x, warrior_y = nx, ny
                    total_moved += 1
                    break

        warrior_position[i] = (warrior_x, warrior_y)

    for i in range(m):
        if warrior_position[i][0] == -1:
            continue

        if warrior_position[i][0] == player_x and warrior_position[i][1] == player_y:
            total_hits += 1
            warrior_position[i] = (-1, -1)

    return total_moved, total_hits

def update_warrior_count_grid(n, m, warrior_position):
    warrior_count_grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        if warrior_position[i][0] == -1: #이미 잡힌 전사
            continue
        x, y = warrior_position[i]
        warrior_count_grid[x][y] += 1

    return warrior_count_grid


assert obstacle_grid[start_x][start_y] == 0, "시작 지점에 장애물이 있습니다."
assert obstacle_grid[end_x][end_y] == 0, "종료 지점에 장애물이 있습니다."

distance_grid = bfs(end_x, end_y, n, obstacle_grid)

current_x, current_y = start_x, start_y  # 현재 플레이어의 위치

sight_map = [[0 for _ in range(n)] for _ in range(n)]

warrior_count_grid = update_warrior_count_grid(n, m, warrior_position)

while True:
    moved = False

    for dx, dy in zip(dxs, dys):
        nx, ny = current_x + dx, current_y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if distance_grid[nx][ny] < distance_grid[current_x][current_y]:
                current_x, current_y = nx, ny
                moved = True
                break
    
    if current_x == end_x and current_y == end_y:
        print("0")
        break

    for i in range(m):
        if warrior_position[i][0] == current_x and warrior_position[i][1] == current_y:
            warrior_position[i] = (-1, -1)
    
    warrior_count_grid = update_warrior_count_grid(n, m, warrior_position)

    sight_coverage = choose_best_sight(current_x, current_y, n, warrior_count_grid, sight_map)

    warrior_moved, warriors_hit = move_warriors(current_x, current_y, n, m, warrior_position, sight_map)

    warrior_count_grid = update_warrior_count_grid(n, m, warrior_position)

    print(f"{warrior_moved} {sight_coverage} {warriors_hit}")