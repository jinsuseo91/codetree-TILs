from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet(range(1, m + 1))

for i in arr:
    s.remove(i)

    print(s[-1])