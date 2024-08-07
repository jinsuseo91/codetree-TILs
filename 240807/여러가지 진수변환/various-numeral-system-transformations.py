n, b = map(int, input().split())
ans = []
num = 0
while True:
    if n < b:
        ans.append(n)
        break
    
    ans.append(n % b)
    n //= b

for i in ans[::-1]:
    print(i, end='')