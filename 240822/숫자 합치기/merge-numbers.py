import heapq

n = int(input())
arr = list(map(int,input().split()))

pq = []
ans = 0

for elem in arr:
    heapq.heappush(pq, elem)

while len(pq) > 1:
    fi = heapq.heappop(pq)
    se = heapq.heappop(pq)
    ans += fi + se
    heapq.heappush(pq, fi + se)

print(ans)