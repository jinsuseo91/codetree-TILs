n, m = map(int, input().split())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))
cnt = 0
#행
for i in range(n):
    hap = 1
    prev_num = d[i][0] 
    for j in range(1, n):
        if prev_num == d[i][j]:
            hap += 1
        else:
            hap = 1
            prev_num = d[i][j]
    if hap >= m:
        cnt += 1
#열
for j in range(n):
    hap = 0
    prev_num = d[0][j] 
    for i in range(1, n):
        if prev_num == d[i][j]:
            hap += 1
        else:
            hap = 1
            prev_num = d[i][j]
    if hap >= m:
        cnt += 1
print(cnt)