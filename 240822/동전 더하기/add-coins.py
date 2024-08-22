n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.reverse()
cnt = 0

for i in arr:
    cnt += k // i
    k %= i
print(cnt)