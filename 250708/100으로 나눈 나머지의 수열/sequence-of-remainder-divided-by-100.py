n = int(input())

def num(a):
    if a == 1:
        return 2
    if a == 2:
        return 4

    return (num(a - 1) * num(a - 2)) % 100

print(num(n))