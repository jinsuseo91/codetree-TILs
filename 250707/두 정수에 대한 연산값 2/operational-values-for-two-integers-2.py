a, b = map(int, input().split())

if a < b:
    a += 10
    b *= 2
    print(a, b)
elif a > b:
    a *= 2
    b += 10
    print(a, b)