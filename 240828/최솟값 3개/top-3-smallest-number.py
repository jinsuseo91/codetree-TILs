import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []
for i in arr:
    heapq.heappush(pq, i)

    if len(pq) <= 2:
        print(-1)
    else:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        c = heapq.heappop(pq)
        print(a*b*c)
        heapq.heappush(pq, a)
        heapq.heappush(pq, b)
        heapq.heappush(pq, c)