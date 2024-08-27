from sortedcontainers import SortedSet

n = int(input())
arr = list(map(int, input().split()))
INT_MAX = float("INF")

s = SortedSet()
ans = INT_MAX

s.add(0)

for i in arr:
    idx = s.bisect_right(i)
    if idx != len(s):
        ans = min(ans, s[idx] - i)

    idx -= 1
    ans = min(ans, i - s[idx])

    s.add(i)
    print(ans)