n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

cnt = 0

for i in range(n):
    if i == 0 or arr[i] != arr[i - 1]:
        cnt += 1
print(cnt)