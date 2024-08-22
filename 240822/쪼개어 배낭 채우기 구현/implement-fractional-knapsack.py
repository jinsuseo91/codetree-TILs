n, m = map(int, input().split())

jew = []

for _ in range(n):
    w, v = map(int, input().split())
    st = v / w
    jew.append([w, v, st])

jew.sort(key = lambda x : x[2], reverse = True)

result = 0.

for i in range(n):
    if jew[i][0] > m:
        result = result + (jew[i][2] * m)
        break
    else:
        result += jew[i][1]
        m -= jew[i][0]
print(f"{result:.3f}")