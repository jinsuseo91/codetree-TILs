import heapq

n, m = map(int, input().split())

arr = list(map(int, input().split()))
pq = []

for elem in arr:
    heapq.heappush(pq, -elem)

for _ in range(m):
    max_val = -heapq.heappop(pq)
    heapq.heappush(pq, -(max_val - 1))
print(-heapq.heappop(pq))