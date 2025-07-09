a, b = map(int, input().split())
arr = list(map(int, input()))
num = 0
for i in range(len(arr)):
    num = num * a + arr[i]
digits = []
while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)
    num //= b

for digit in digits[::-1]:
    print(digit, end='')