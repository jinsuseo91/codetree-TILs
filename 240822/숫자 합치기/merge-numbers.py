n = int(input())

arr = list(map(int,input().split()))

arr.sort()
cnt = 0
result = []
for i in range(n):
    if i == 0:
        cnt += arr[i]
    else:            
        cnt += arr[i]
        result.append(cnt)
print(sum(result))