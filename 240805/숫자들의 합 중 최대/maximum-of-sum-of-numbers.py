x, y = map(int, input().split())

max_cnt = 0
for i in range(x, y + 1):
    cnt = 0
    i = str(i)
    for j in range(len(i)):
        cnt += int(i[j])
    max_cnt = max(max_cnt, cnt)

print(max_cnt)