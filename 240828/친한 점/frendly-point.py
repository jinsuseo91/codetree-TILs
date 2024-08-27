from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr1 = [tuple(map(int, input().split())) for _ in range(m)]

s = SortedSet(arr)

for i in arr1:
    idx = s.bisect_left(i)
    if idx == len(s):
        print(-1, -1)
    else:
        x, y = s[idx]
        print(x, y)