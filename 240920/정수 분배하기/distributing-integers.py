MAX_NUM = 100000

n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

def is_possible(k):
    cnt = 0
    for elem in arr:
        cnt += elem // k

    return cnt >= m

left = 1
right = MAX_NUM
ans = 0
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1
print(ans)