n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
def can_d(d):
    cnt = 1
    last_position = arr[0]

    for i in range(1, n):
        if arr[i] - last_position >= d:
            cnt += 1
            last_position = arr[i]
        if cnt >= m:
            return True
    return False

left, right = 1, arr[-1] - arr[0]
ans = 0

while left <= right:
    mid = (left + right)//2
    if can_d(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)