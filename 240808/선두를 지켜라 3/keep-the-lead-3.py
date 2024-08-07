n, m = map(int, input().split())
a_d, b_d = [0], [0]

def make_dist(player, p_dist):
    for i in range(player):
        velocity, time = map(int, input().split())
        for _ in range(time):
            p_dist.append(velocity + p_dist[-1])

make_dist(n, a_d)
make_dist(m, b_d)

a_d += [a_d[-1]] * (max_length - len(a_d))
b_d += [b_d[-1]] * (max_length - len(b_d))

compare = [a_d[i] - b_d[i] for i in range(len(a_d))][1:]
answer = 0

for idx in range(1, len(compare)):
    if compare[idx] * compare[idx - 1] <= 0:
        answer += 1

print(answer)