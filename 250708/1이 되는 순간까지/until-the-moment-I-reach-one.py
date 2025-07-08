n = int(input())

def until_1(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        n //= 2
    else:
        n //= 3
    return until_1(n) + 1

print(until_1(n))