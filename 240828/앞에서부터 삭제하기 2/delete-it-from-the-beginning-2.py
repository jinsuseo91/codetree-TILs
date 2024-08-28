import heapq
n = int(input())
arr = list(map(int, input().split()))
pq = []

sum_ = 0
max_ = 0
heapq.heappush(pq, arr[n-1])
sum_ += arr[n - 1]
for i in range(n-2, 0, -1):
    heapq.heappush(pq, arr[i])
    sum_ += arr[i]
    min_ = pq[0]
    avg = (sum_ - min_) / (n - i - 1)

    if max_ < avg:
        max_ = avg
print(f"{max_:.2f}")