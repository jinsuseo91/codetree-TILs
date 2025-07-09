n = int(input())
arr = [list(input()) for _ in range(n)]

cnt = 1

for i in range(len(arr) - 1):
    if arr[i] != arr[i + 1]:
        cnt += 1

print(cnt)