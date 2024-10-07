n = int(input())
ans = 0
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((y,x))

arr.sort()

li, ri = 0, n - 1
while li <= ri:
    ly, lx = arr[li]
    ry, rx = arr[ri]

    ans = max(ans, ly + ry)

    if lx < rx:
        arr[ri] = (ry, rx - lx)
        li += 1
    elif lx > rx:
        arr[li] = (ly, lx - rx)
        ri -= 1
    else:
        li += 1
        ri -= 1
print(ans)