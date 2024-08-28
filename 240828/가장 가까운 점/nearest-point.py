import heapq

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pq = []

for x, y in arr:
    heapq.heappush(pq, (x + y, x, y))

for _ in range(m):
    _, x, y = heapq.heappop(pq)
    x, y = x + 2, y + 2
    heapq.heappush(pq, (x + y, x, y))
_, last_x, last_y = heapq.heappop(pq)
print(last_x, last_y)