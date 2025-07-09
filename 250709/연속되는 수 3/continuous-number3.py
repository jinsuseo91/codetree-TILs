n = int(input())
arr = (int(input()) for _ in range(n))

max_ = 0
cnt = 1
arr = list(arr)

for i in range(n):
    if arr[i] > 0:
        arr[i] = 1
    elif arr[i] < 0:
        arr[i] = 0

for i in range(1, n):
    if arr[i] == arr[i - 1]:
        cnt += 1
        max_ = max(cnt, max_)

    else:
        cnt = 1

print(max_)