n, t = map(int, input().split())

ary1 = list(map(int, input().split()))
ary2 = list(map(int, input().split()))
ary3 = list(map(int, input().split()))

ary = ary1 + ary2 + ary3

for i in range(t):
    temp = ary[-1]
    for k in range(3*n-1, 0, -1):
        ary[k] = ary[k-1]
    ary[0] = temp

print(*ary[0:n])
print(*ary[n:2*n])
print(*ary[2*n:3*n])