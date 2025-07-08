a, b, c = map(int, input().split())

result = (a - 11) * 24 * 60
num1 = b * 60 + c
num2 = 11 * 60 + 11

result += (num1 - num2)

print(result)