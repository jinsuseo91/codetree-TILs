import heapq
n = int(input())

arr = [int(input()) for _ in range(n)]
pq = []

for i in arr:
    if i == 0:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq, i)