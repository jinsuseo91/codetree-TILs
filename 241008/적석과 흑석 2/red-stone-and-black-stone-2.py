c, n =map(int, input().split())
red = [int(input()) for _ in range(c)]
black = []
for _ in range(n):
    a, b = map(int, input().split())
    black.append((b, a))
red.sort()
black.sort()

ans = 0

for b, a in black:
    for i in range(len(red)):
        if a <= red[i] <= b:
            ans += 1
            red.pop(i)
            break

print(ans)