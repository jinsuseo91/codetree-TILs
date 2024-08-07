n, t = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0
max_ = 0
for i in range(len(arr)):
    if arr[i] > t:
        cnt += 1
    else:
        cnt = 0
    max_ = max(max_, cnt)
print(max_)