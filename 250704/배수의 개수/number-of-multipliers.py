result3, result5 = 0, 0

for _ in range(10):
    a = int(input())

    if a % 3 == 0:
        result3 += 1
    if a % 5 == 0:
        result5 += 1

print(result3, result5)