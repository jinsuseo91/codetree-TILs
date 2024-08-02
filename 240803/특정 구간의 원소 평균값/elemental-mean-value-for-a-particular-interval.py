n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        sum_ = 0
        cnt_ = 0
        for k in range(i, j + 1):
            sum_ += arr[k]
            cnt_ += 1
        avg = sum_ // cnt_
        if avg in arr:
            cnt += 1

print(cnt)