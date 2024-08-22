n = int(input())

arr = list(map(int,input().split()))

arr.sort()
cnt = 0
result = []
for i in range(n):
    cnt += arr[i]
    result.append(cnt)
print(sum(result)-arr[0])