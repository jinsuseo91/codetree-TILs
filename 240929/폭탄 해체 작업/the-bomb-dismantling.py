import heapq
max_t = 10000

n = int(input())
bomb = []
for _ in range(n):
    score, time_limit = map(int, input().split())
    bomb.append((time_limit, score))

def get_time_limit(bomb_idx):
    time_limit, _ = bomb[bomb_idx]
    return time_limit

def get_score(bomb_idx):
    _, score = bomb[bomb_idx]
    return score

bomb.sort()

pq = []
bomb_idx = n - 1
ans = 0
for t in range(max_t, 0, -1):
    while bomb_idx >= 0 and get_time_limit(bomb_idx) >= t:
        heapq.heappush(pq, -get_score(bomb_idx))
        bomb_idx -= 1

    if pq:
        ans += -heapq.heappop(pq)
print(ans)