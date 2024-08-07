arr = list(map(int, input()))
num = 0
for i in range(len(arr)):
    num = num * 2 + arr[i]

num *= 17
ans = []
while True:
    if num < 2:
        ans.append(num)
        break

    ans.append(num % 2)
    num //= 2

for i in ans[::-1]:
    print(i, end='')