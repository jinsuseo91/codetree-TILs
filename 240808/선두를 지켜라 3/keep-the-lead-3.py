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

# 두 사람이 동일한 위치에 있는지 확인하는 함수
def check_meeting(a_d, b_d):
    meet_count = 0
    for i in range(1, len(a_d)):
        if a_d[i] == b_d[i] or (a_d[i] - b_d[i]) * (a_d[i - 1] - b_d[i - 1]) < 0:
            meet_count += 1
    return meet_count

result = check_meeting(a_d, b_d)
print(result)