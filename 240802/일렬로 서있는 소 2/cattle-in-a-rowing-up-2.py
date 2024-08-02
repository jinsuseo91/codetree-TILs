n = int(input())

arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a, b, c = arr[i], arr[j], arr[k]
            if a < b and b < c:
                cnt += 1
print(cnt)