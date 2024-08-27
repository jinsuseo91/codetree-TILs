from sortedcontainers import SortedSet

n, m = map(int, input().split())

arr = list(map(int, input().split()))

s = SortedSet(range(1, m + 1))

ans = 0

for i in arr:
    idx = s.bisect_right(i)
    if idx != 0:
        idx -= 1
        s.remove(s[idx])
        ans += 1
    else:
        break
print(ans)