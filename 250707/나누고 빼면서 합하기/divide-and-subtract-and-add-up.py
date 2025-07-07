n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = []
while m != 0:
    arr2.append(m)
    if m % 2 == 1:
        m -= 1
    elif m % 2 == 0:
        m //= 2
result = 0
for i in arr2:
    result += arr[i - 1]
print(result)