n = int(input())
k = int(input())

left, right = 1, n * n
ans = right

while left <= right:
    mid = (left + right) // 2

    val = 0
    for i in range(1, n + 1):
        val += min(n, mid // i)

    if val >= k:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
print(ans)