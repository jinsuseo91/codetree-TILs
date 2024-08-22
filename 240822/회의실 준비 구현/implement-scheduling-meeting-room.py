n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key = lambda x : (x[1], x[0]))

total = 0
last = 0
for i in range(n):
    if arr[i][0] < last:
        continue
    if arr[i][1] >= last:
        total += 1
        last = arr[i][1]
print(total)