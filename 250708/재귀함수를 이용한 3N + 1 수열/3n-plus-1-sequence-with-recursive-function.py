n = int(input())

def num(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return num(n // 2) + 1
    else:
        return num(n*3 + 1) + 1
print(num(n))