n = int(input())

arr = [int(input()) for _ in range(n)]
cnt = 0
max_ = 0
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        cnt += 1
        max_ = max(cnt, max_)
    else:
        cnt = 1
print(max_)