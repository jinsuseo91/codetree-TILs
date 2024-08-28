import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []

for elem in arr:
    heapq.heappush(pq, -elem)

while (len(pq) >= 2):
        x = -heapq.heappop(pq)
        y = -heapq.heappop(pq)
        if (x-y) != 0:
            heapq.heappush(pq, -abs(x - y))

if len(pq) == 1:
    print(-heapq.heappop(pq))
else:
    print(-1)