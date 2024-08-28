import heapq

n = int(input())
arr = [int(input()) for _ in range(n)]
pq = []

for elem in arr:
    if elem != 0:
        heapq.heappush(pq, -elem)
    
    else:
        if not pq:
            print(0)
        else:
            print(-heapq.heappop(pq))