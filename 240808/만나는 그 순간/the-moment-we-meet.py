# 입력 받기
N, M = map(int, input().split())

# A와 B의 이동 명령을 입력받아 리스트로 저장
A_moves = [input().split() for _ in range(N)]
B_moves = [input().split() for _ in range(M)]

# 명령을 (방향, 시간)으로 변환
A_moves = [(d, int(t)) for d, t in A_moves]
B_moves = [(d, int(t)) for d, t in B_moves]

# 초기 위치
A_pos = 0
B_pos = 0

# 각자의 시간 카운터
A_time = 0
B_time = 0

# A와 B의 이동 리스트를 시간별로 변환
A_positions = []
B_positions = []

# A의 이동을 시간별로 기록
for direction, time in A_moves:
    for _ in range(time):
        if direction == 'R':
            A_pos += 1
        else:
            A_pos -= 1
        A_positions.append(A_pos)

# B의 이동을 시간별로 기록
for direction, time in B_moves:
    for _ in range(time):
        if direction == 'R':
            B_pos += 1
        else:
            B_pos -= 1
        B_positions.append(B_pos)

# 두 사람이 움직인 시간의 최대값을 구한다
max_time = max(len(A_positions), len(B_positions))

# 시간을 돌면서 처음 만나는 시간을 찾는다
for t in range(max_time):
    # A와 B의 위치가 다르면 -1로 처리
    A_current_pos = A_positions[t] if t < len(A_positions) else A_positions[-1]
    B_current_pos = B_positions[t] if t < len(B_positions) else B_positions[-1]
    
    if A_current_pos == B_current_pos:
        print(t + 1)
        break
else:
    print(-1)