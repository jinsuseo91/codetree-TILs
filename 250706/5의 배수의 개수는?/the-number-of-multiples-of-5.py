arr = [list(map(int, input().split())) for _ in range(4)]

result = 0

for i in range(4):
    for j in range(4):
        if arr[i][j] % 5 == 0:
            result += 1
print(result)