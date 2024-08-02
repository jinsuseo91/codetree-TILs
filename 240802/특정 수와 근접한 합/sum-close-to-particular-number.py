import sys

MAX_INT = sys.maxsize

n, s = map(int, input().split())
arr = list(map(int, input().split()))

total_sum = sum(arr)

min_val = MAX_INT
for i in range(n):
    for j in range(i + 1, n):
        sum_val = total_sum - (arr[i] + arr[j])
        diff = abs(s - sum_val)

        min_val = min(min_val, diff)

print(min_val)