n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        sum_ = 0
        for k in range(i, j + 1):
            sum_ += arr[k]
        avg = sum_ / (j - i + 1)
        exists = False
        for k in range(i, j + 1):
            if arr[k] == avg:
                exists = True

        if exists:
            cnt += 1

print(cnt)