n, k = map(int,input().split())
arr = list(map(int, input().split()))
max_sum = 0
a = 0

for i in range(n - k + 1):
    sum_ = 0
    for j in range(i, i + k):
        sum_ += arr[j]
    max_sum = max(max_sum, sum_)
    # a = max(max_sum, a)
print(max_sum)