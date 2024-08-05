n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
num_gold = 0

for i in range(n - 2):
    for j in range(n - 2):
        num_gold = array[i][j] + array[i+1][j] + array[i+2][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1] + array[i+2][j+1] + array[i+1][j+2] + array[i+2][j+2]
        if num_gold > max_cnt:
            max_cnt = num_gold
print(max_cnt)