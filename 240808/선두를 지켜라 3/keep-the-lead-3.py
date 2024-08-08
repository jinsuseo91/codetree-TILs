N, M = map(int, input().split())
a_dist, b_dist = [0], [0]

def make_dist(player, p_dist):
    for i in range(player):
        velocity, times = map(int, input().split())
        for _ in range(times):
            p_dist.append(velocity + p_dist[-1])

make_dist(N, a_dist)
make_dist(M, b_dist)

compare = [a_dist[i] - b_dist[i] for i in range(len(a_dist))][1:]
answer = 0

for idx in range(1, len(compare)):
    if compare[idx] * compare[idx - 1] <= 0:
        answer += 1

print(answer)