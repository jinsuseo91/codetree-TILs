n = int(input())
arr = list(map(int, input().split()))

result = 0

for i in range(n - 1):
    if arr[i] == 0:
        result += 1
        arr[i] = 1
        arr[i + 1] = 1 - arr[i + 1]
        #arr[i - 1] = 1 - arr[i - 1]
if all(arr):
    print(result)
else:
    print(-1)