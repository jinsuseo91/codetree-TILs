arr1 = [list(map(int, input().split())) for _ in range(4)]

arr2 = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]
result = 0

for i in range(4):
    for j in range(4):
        if arr2[i][j] == 1:
            result += arr1[i][j]

print(result)