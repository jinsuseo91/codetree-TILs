n, m = map(int, input().split())
d = []
cnt = 0
for _ in range(n):
    row = list(map(int, input().split()))
    d.append(row)
    for i in range(n - m + 1):
        if row[i:i+m].count(row[i]) == m:
            cnt += 1
            break
#열
for j in zip(*d):
    for i in range(n-m+1):
        if j[i:i+m].count(j[i]) == m:
            cnt += 1
            break
print(cnt)