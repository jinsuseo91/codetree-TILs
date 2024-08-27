from sortedcontainers import SortedSet

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr1 = [int(input()) for _ in range(m)]

s = SortedSet(arr)

for num in arr1:
    idx = s.bisect_left(num)
    if idx == len(s):
        print(-1)
    else:
        print(s[idx])