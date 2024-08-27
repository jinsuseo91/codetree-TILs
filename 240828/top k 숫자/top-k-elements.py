from sortedcontainers import SortedSet

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet()
arr.sort(reverse = True)
arr = list(set(arr))

for i in range(k):
    print(arr[i], end=" ")