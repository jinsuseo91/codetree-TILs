x, y = map(int, input().split())
cnt = 0
for i in range(x, y + 1):
    i = str(i)
    k = i[::-1]
    if i == k:
        cnt += 1
print(cnt)