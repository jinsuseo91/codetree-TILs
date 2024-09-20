n, m = map(int, input().split())
times = [int(input()) for _ in range(m)]

left, right = 1, max(times) * n

def pass_(t):
    tot = 0
    for time in times:
        tot += t // time
        if tot >= n:
            return True
    return tot >= n

ans = right
while left <= right:
    mid = (left + right)//2
    if pass_(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)