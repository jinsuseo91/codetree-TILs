n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    result = 0
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    for i in range(a, b + 1):
        result += arr[i]
    print(result)