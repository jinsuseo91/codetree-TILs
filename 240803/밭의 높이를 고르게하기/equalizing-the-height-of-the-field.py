n, h, t = map(int, input().split())

arr = list(map(int,input().split()))

ans = 100000
for i in range(n):
    cnt = 0
    for j in range(i, i + t):
        if 0 <= j <= n - 1:
            cnt += abs(arr[j] - h)
    ans = min(cnt, ans)
print(ans)