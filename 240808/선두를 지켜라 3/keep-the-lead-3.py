n, m = map(int, input().split())
a_moves, b_moves = [], []

# A의 이동 명령을 입력받아 리스트로 저장
for _ in range(n):
    v, t = map(int, input().split())
    a_moves.append((v, t))

# B의 이동 명령을 입력받아 리스트로 저장
for _ in range(m):
    v, t = map(int, input().split())
    b_moves.append((v, t))

# A와 B의 위치를 추적할 리스트 초기화
a_pos, b_pos = [0], [0]

# A의 이동을 시간별로 기록
for v, t in a_moves:
    for _ in range(t):
        a_pos.append(a_pos[-1] + v)

# B의 이동을 시간별로 기록
for v, t in b_moves:
    for _ in range(t):
        b_pos.append(b_pos[-1] + v)

# 두 리스트의 길이를 맞춤
max_length = max(len(a_pos), len(b_pos))
a_pos += [a_pos[-1]] * (max_length - len(a_pos))
b_pos += [b_pos[-1]] * (max_length - len(b_pos))

# 교차점을 찾기 위한 변수 초기화
crossings = 0

# 두 사람이 동일한 위치에 있는지 확인
for i in range(1, max_length):
    if a_pos[i] == b_pos[i] or (a_pos[i] - b_pos[i]) * (a_pos[i - 1] - b_pos[i - 1]) < 0:
        crossings += 1

print(crossings)