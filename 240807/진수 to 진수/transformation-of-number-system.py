a, b = map(int, input().split())
ans = []
arr = list(map(int, input()))
num = 0

for i in range(len(arr)):
    num = num * a + arr[i]

while True:
    if num < b:
        ans.append(num)
        break
    ans.append(num % b)
    num //= b

for i in ans[::-1]:
    print(i, end ='')