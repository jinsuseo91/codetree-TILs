n = int(input())

arr = [int(input()) for _ in range(n)]

cnt = 0
max_ = 0
for i in range(len(arr)):
    # 곱했을 때 0보다 크면 무조건 같다
    if i > 0 and arr[i] * arr[i-1] > 0:
        cnt += 1
    else:
        cnt = 1
    max_ = max(max_, cnt)
print(max_)