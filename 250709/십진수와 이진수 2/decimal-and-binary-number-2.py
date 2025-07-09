arr = list(map(int, input()))
num = 0

for i in range(len(arr)):
    num = num * 2 + arr[i]

n = num * 17
digits = []

while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

for digit in digits[::-1]:
    print(digit, end='')