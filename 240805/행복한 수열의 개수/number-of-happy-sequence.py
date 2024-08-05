n, m = map(int, input().split())
arr = []

cnt = 0

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for i in range(n - m + 1):
        if row[i: i + m].count(row[i]) == m:
            cnt += 1
            break
for j in zip(*arr):
    for i in range(n - m + 1):
        if j[i:i + m].count(j[i]) == m:
            cnt += 1
            break
print(cnt)