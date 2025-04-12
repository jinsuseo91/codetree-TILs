N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr3 = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
wall = [list(map(int, input().split())) for _ in range(F)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def find_3d_start():
    for i in range(M):
        for j in range(M):
            if arr3[4][i][j] == 2:
                return 4, i, j

def find_2d_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 4:
                arr[i][j] = 0
                return i, j

def find_3d_base():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                return i, j

def find_3d_end_2d_start():
    bi, bj = find_3d_base()

    for i in range(bi, bi + M):
        for j in range(bj, bj + M):
            if arr[i][j] != 3:
                continue

            if arr[i][j + 1] == 0:  #우측에 출구
                return 0, M - 1, (M-1) - (i - bi), i, j + 1
            elif arr[i][j - 1] == 0: #좌측에 출구
                return 1, M - 1, i-bi, i, j - 1
            elif arr[i + 1][j] == 0: #남
                return 2, M - 1, j - bj, i + 1, j
            elif arr[i - 1][j] == 0: #북
                return 3, M - 1, (M - 1) - (j - bj), i - 1, j
    return -1

left_nxt = {0:2, 2:1, 1:3, 3:0}
right_nxt = {0:3, 2:0, 1:2, 3:1}

from collections import deque
def bfs_3d(sk, si, sj, ek, ei, ej):
    q = deque()
    v = [[[0] * M for _ in range(M)] for _ in range(5)]

    q.append((sk, si, sj))
    v[sk][si][sj] = 1

    while q:
        ck, ci, cj = q.popleft()

        if (ck, ci, cj) == (ek, ei, ej):
            return v[ck][ci][cj]

        #네 방향, 범위 내/범위 밖 -> 다른 평면 이동 처리
        for di, dj in zip(dxs, dys):
            ni, nj = ci + di, cj + dj
            #범위 밖일 때
            if ni < 0: #위쪽으로 이동할 때
                if ck == 0: #현재 우측 평면일 때
                    nk = 4
                    ni = (M - 1) - cj
                    nj = M - 1
                elif ck == 1: #현재 좌측평면일 때
                    nk = 4
                    ni = cj
                    nj = 0
                elif ck == 2: #현재 남측
                    nk = 4
                    ni = M - 1
                    nj = cj
                elif ck == 3:
                    nk = 4
                    ni = 0
                    nj = (M - 1) - cj
                elif ck == 4:
                    nk = 3
                    ni = 0
                    nj = (M - 1) - cj

            elif ni >= M: #아래쪽
                if ck == 4:
                    nk = 2
                    ni = 0
                    nj = cj
                else:
                    continue
            elif nj < 0: #왼쪽
                if ck == 4:
                    nk = 1
                    ni = 0
                    nj = ci
                else:
                    nk = left_nxt[ck]
                    ni = ci
                    nj = M - 1
            elif nj >= M: #오른쪽
                if ck == 4:
                    nk = 0
                    ni = 0
                    nj = (M - 1) - cj
                else:
                    nk = right_nxt[ck]
                    ni = ci
                    nj = 0
            else:
                nk = ck

            # #미방문, 조건에 맞으면
            # if v[nk][ni][nj] == 0 and arr3[nk][ni][nj] == 0:
            #     q.append((nk, ni, nj))
            #     v[nk][ni][nj] = v[ck][ci][cj] + 1
            if v[nk][ni][nj]==0 and arr3[nk][ni][nj]==0:
                q.append((nk,ni,nj))
                v[nk][ni][nj]=v[ck][ci][cj]+1
    return -1

def bfs_2d(v, dist, si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    v[si][sj] = dist

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            return v[ci][cj]

        for di, dj in zip(dxs, dys):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and v[ci][cj] + 1 < v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return -1

# [1] 주요 위치 찾기
# 3차원 시작, 3차원 끝, 2차원 시작, 2차원 끝
sk_3d, si_3d, sj_3d = find_3d_start()
ei, ej = find_2d_start()
ek_3d, ei_3d, ej_3d, si, sj = find_3d_end_2d_start()

di=[ 0, 0, 1,-1]
dj=[ 1,-1, 0, 0]
# [2] 3차원 공간 탐색 : 시작 위치 -> 탈출위치 거리 탐색(BFS 최단거리)
dist = bfs_3d(sk_3d, si_3d, sj_3d, ek_3d, ei_3d, ej_3d)

if dist != -1:
    # [3] 2차원 탐색 준비 : 시간 이상 현상 처리해서 v에 시간 표시
    v = [[401] * N for _ in range(N)]
    for wi, wj, wd, wv in wall:
        v[wi][wj] = 1
        for mul in range(1, N + 1):
            wi, wj = wi + di[wd], wj + dj[wd]
            if 0 <= wi < N and 0 <= wj < N and arr[wi][wj] == 0 and (wi, wj) != (ei, ej):
                if v[wi][wj] > wv * mul:
                    v[wi][wj] = wv * mul
            else:
                break

    # [4] 2차원 시작 위치에서 bfs로 탈출구 탐색(v에 적혀있는 값보다 작아야 통과)
    dist = bfs_2d(v, dist, si, sj, ei, ej)

print(dist)