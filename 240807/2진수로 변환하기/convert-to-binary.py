n = int(input())
ans = []

while True:
    if n < 2:
        ans.append(n)
        break
    
    ans.append(n%2)
    n //= 2
for i in ans[::-1]:
    print(i, end='')