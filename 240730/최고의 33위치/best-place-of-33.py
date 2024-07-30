n = int(input())
array = []
cnt = 0
max_cnt = 0
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n - 2):
    for j in range(n - 2):
        cnt = array[i][j] + array[i+1][j] + array[i+2][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1] + array[i+2][j+1] + array[i+1][j+2] + array[i+2][j+2]
        if cnt > max_cnt:
            max_cnt = cnt
print(max_cnt)