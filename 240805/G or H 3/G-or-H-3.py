n, k = list(map(int, input().split()))

max_num = 10000
arr = [0] * (max_num + 1)

for _ in range(n):
    x, c = list(input().split())
    x = int(x)

    arr[x] = 1 if c == 'G' else 2

max_sum = 0
for i in range(max_num - k + 1):

    sum_interval = 0
    for j in range(i, i + k + 1):
        sum_interval += arr[j]

    max_sum = max(max_sum, sum_interval)
print(max_sum)