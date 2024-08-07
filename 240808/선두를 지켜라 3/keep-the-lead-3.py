n, m = map(int, input().split())
a_d, b_d = [0], [0]  # A와 B의 초기 위치를 0으로 설정

def make_dist(player, p_dist):
    for _ in range(player):
        velocity, time = map(int, input().split())
        for _ in range(time):
            p_dist.append(velocity + p_dist[-1])  # 이전 위치에 속도를 더하여 새로운 위치를 추가

make_dist(n, a_d)
make_dist(m, b_d)

# 비교를 위해 두 거리 리스트의 길이를 맞춘다
max_length = max(len(a_d), len(b_d))
a_d += [a_d[-1]] * (max_length - len(a_d))
b_d += [b_d[-1]] * (max_length - len(b_d))

compare = [a_d[i] - b_d[i] for i in range(max_length)][1:]  # 첫번째 요소는 제외
answer = 0

for idx in range(1, len(compare)):
    if compare[idx] * compare[idx - 1] <= 0:  # 방향이 바뀌는 순간을 체크
        answer += 1

print(answer)