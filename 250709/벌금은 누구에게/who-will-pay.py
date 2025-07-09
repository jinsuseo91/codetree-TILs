n, m, k = map(int, input().split())
arr = [0] * (n + 1)
ans = -1
for _ in range(m):
    a = int(input())
    arr[a] += 1

    if arr[a] >= k:
        ans = a
        break
print(ans)