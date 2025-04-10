import sys
import threading

MAXN = 20
MAXM = 20
MAXF = 400
MAXP = MAXF*6

INF = int(1e9+10)

SpaceMap = [[0 for _ in range(MAXN+10)] for _ in range(MAXN+10)] #미지의 공간 평면도
SpaceMapCellID = [[0 for _ in range(MAXN+10)] for _ in range(MAXN+10)] #평면도의 각 셀에 대응하는 그래프 정점의 번호를 저장
TimeWall = [[[0 for _ in range(MAXM+10)] for _ in range(MAXM+10)] for _ in range(6)] #시간의 벽의 단면도
TimeWallCellID = [[[0 for _ in range(MAXM+10)] for _ in range(MAXM+10)] for _ in range(6)] # 시간의 벽의 단면도의 각 셀에 대응하는 그래프 정점의 번호를 저장

class AbnormalTimeEvent:
    #시간이상 현상이 시작점의 행번호, 열번호, 방향, 확장 주기, 시간 이상 현상의 진행 여부를 차례로 저장
    def __init__(self, xpos=0, ypos=0, direction=0, cycle=0, alive=0):
        self.xpos = xpos
        self.ypos = ypos
        self.direction = direction
        self.cycle = cycle
        self.alive = alive

events = [AbnormalTimeEvent() for _ in range(MAXF+10)]

Graph = []

def build_graph(N, M):
    global Graph, SpaceMapCellID, TimeWallCellID
    cnt = 0

    for i in range(N):
        for j in range(N):
            if SpaceMap[i][j] != 3:
                cnt += 1
                SpaceMapCellID[i][j] = cnt
    
    for t in range(5):
        for i in range(M):
            for j in range(M):
                cnt += 1
                TimeWallCellID[t][i][j] = cnt

    Graph = [[-1 for _ in range(4)] for _ in range(cnt + 1)]
    #동남서북 순서로
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            if SpaceMap[i][j] != 3: #장애물 없을 때
                idx = SpaceMapCellID[i][j]
                for dd in range(4):
                    nx = i + dx[dd]
                    ny = j + dy[dd]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N: #범위를 벗어나거나
                        continue
                    if SpaceMap[nx][ny] == 3: #장애물이 있는 경우
                        continue
                    Graph[idx][dd] = SpaceMapCellID[nx][ny]

        for t in range(4):
            for i in range(M):
                for j in range(M):
                    idx = TimeWallCellID[t][i][j]
                    for dd in range(4):
                        nx, ny = i + dx[dd], j + dy[dd]
                        if nx < 0 or nx >= M:
                            continue
                        if ny < 0:
                            Graph[idx][dd] = TimeWallCellID[(t + 1)% 4][nx][M - 1]
                        elif ny >= M:
                            Graph[idx][dd] = TimeWallCellID[(t + 3)% 4][nx][0]
                        else:
                            Graph[idx][dd] = TimeWallCellID[t][nx][ny]

        for i in range(M):
            for j in range(M):
                idx = TimeWallCellID[4][i][j]
                for dd in range(4):
                    nx, ny = i + dx[dd], j + dy[dd]
                    if nx < 0 or ny < 0 or nx >= M or ny >= M:
                        continue
                    Graph[idx][dd] = TimeWallCellID[4][nx][ny]

    for i in range(M):
        idx = TimeWallCellID[4][i][M - 1]
        idy = TimeWallCellID[0][0][M - 1 - i]
        Graph[idx][0] = idy
        Graph[idy][3] = idx
    for i in range(M):
        idx = TimeWallCellID[4][M - 1][i]
        idy = TimeWallCellID[1][0][i]
        Graph[idx][1] = idy
        Graph[idy][3] = idx
    for i in range(M):
        idx = TimeWallCellID[4][i][0]
        idy = TimeWallCellID[2][0][i]
        Graph[idx][2] = idy
        Graph[idy][3] = idx
    for i in range(M):
        idx = TimeWallCellID[4][0][i]
        idy = TimeWallCellID[3][0][M - 1 - i]
        Graph[idx][3] = idy
        Graph[idy][3] = idx

    #평면도에서 시간의 벽이 시작하는 셀 행, 열
    timewallStartx = -1
    timewallStarty = -1

    for i in range(N):
        for j in range(N):
            if SpaceMap[i][j] == 3:
                timewallStartx = i
                timewallStarty = j
                break
        if timewallStartx != -1:
            break

    if timewallStarty + M < N: #평면도 범위안이면
        for i in range(M):
            idx = TimeWallCellID[0][M - 1][i]
            idy = SpaceMapCellID[timewallStartx + (M - 1) - i][timewallStarty + M]
            Graph[idx][1] = idy
            Graph[idy][2] = idx
    if timewallStartx + M < N:
        for i in range(M):
            idx = TimeWallCellID[1][M - 1][i]
            idy = SpaceMapCellID[timewallStartx + M][timewallStarty + i]
            Graph[idx][1] = idy
            Graph[idy][3] = idx
    if timewallStarty > 0:
        for i in range(M):
            idx = TimeWallCellID[2][M - 1][i]
            idy = SpaceMapCellID[timewallStartx + i][timewallStarty - 1]
            Graph[idx][1] = idy
            Graph[idy][0] = idx
    if timewallStartx > 0:
        for i in range(M):
            idx = TimeWallCellID[3][M - 1][i]
            idy = SpaceMapCellID[timewallStartx - 1][timewallStarty + (M - 1) - i]
            Graph[idx][1] = idy
            Graph[idy][1] = idx
    
    return cnt #그래프 끝번호

N, M, E = map(int, input().split())

for i in range(N):
    SpaceMap[i][:N] = list(map(int, input().split()))

for i in range(M):
    TimeWall[0][i][:M] = list(map(int, input().split()))

for i in range(M):
    TimeWall[2][i][:M] = list(map(int, input().split()))

for i in range(M):
    TimeWall[1][i][:M] = list(map(int, input().split()))

for i in range(M):
    TimeWall[3][i][:M] = list(map(int, input().split()))

for i in range(M):
    TimeWall[4][i][:M] = list(map(int, input().split()))

for i in range(1, E + 1):
    x, y, direction, cycle = map(int, input().split())
    events[i].xpos = x
    events[i].ypos = y
    events[i].direction = direction
    events[i].cycle = cycle
    if events[i].direction == 1:
        events[i].direction = 2
    elif events[i].direction == 2:
        events[i].direction = 1
    events[i].alive = 1

cnt = build_graph(N, M)
dist = [-1] * (cnt + 1)

for i in range(N):
    for j in range(N):
        if SpaceMap[i][j] == 3:
            continue
        if SpaceMap[i][j] == 1:
            idx = SpaceMapCellID[i][j]
            dist[idx] =INF

#이상현상 발생한 곳도 장애물 처리
for i in range(1, E + 1):
    x = events[i].xpos
    y = events[i].ypos
    idx = SpaceMapCellID[x][y]
    dist[idx] = INF

for t in range(5):
    for i in range(M):
        for j in range(M):
            if TimeWall[t][i][j] == 1:
                idx = TimeWallCellID[t][i][j]
                dist[idx] = INF

from collections import deque

q = deque()

cell_start = -1
cell_end = -1
#탈출 지점
for i in range(N):
    for j in range(N):
        if SpaceMap[i][j] == 4:
            cell_end = SpaceMapCellID[i][j]
            break
    if cell_end != -1:
        break
#시작지점
for i in range(M):
    for j in range(M):
        if TimeWall[4][i][j] == 2:
            cell_start = TimeWallCellID[4][i][j]
            break
    if cell_start != -1:
        break

q.append(cell_start)
dist[cell_start] = 0

runs = 1

while True:
    for i in range(1, E + 1):
        if not events[i].alive: #죽었으면 넘어가
            continue
        if runs % events[i].cycle: #주기의 배수가 아니면 넘어가
            continue
        #이상현상이 도달한 좌표 nx,ny
        nx = events[i].xpos
        ny = events[i].ypos
        steps = runs // events[i].cycle
        if events[i].direction == 0:
            ny += steps
        elif events[i].direction == 1:
            nx += steps
        elif events[i].direction == 2:
            ny -= steps
        else:
            nx -= steps
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            events[i].alive = 0
            continue
        if SpaceMap[nx][ny]: #1이면 장애물있는 칸
            events[i].alive = 0
            continue
        idx = SpaceMapCellID[nx][ny]
        dist[idx] = INF

    #이번턴에 도달가능한 셀들의 번호를 저장할 리스트
    next_cells = []
    size = len(q)
    for _ in range(size):
        idx = q.popleft()
        for i in range(4):
            idy = Graph[idx][i]
            if idy == -1:
                continue
            if dist[idy] != -1:
                continue
            dist[idy] = runs
            next_cells.append(idy)

    if not next_cells:
        break
    q.extend(next_cells)
    if dist[cell_end] != -1:
        break
    runs += 1

#정답 출력
if dist[cell_end] == -1 or dist[cell_end] >= INF:
    print(-1)
else:
    print(dist[cell_end])