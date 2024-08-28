import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []

for elem in arr:
    heapq.heappush(pq, -elem)

while True:
    if len(pq) == 1:
        print(pq[0])
        break
    elif len(pq) == 0:
        print(-1)
        break
    else:
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)
        heapq.heappush(pq, abs(x - y))