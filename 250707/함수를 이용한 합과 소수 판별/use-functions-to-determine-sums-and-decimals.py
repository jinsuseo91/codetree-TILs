a, b = map(int, input().split())

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True
cnt = 0
def num(n):
    if is_prime(n):
        if ((n // 10) + (n % 10)) % 2 == 0:
            return True
    return False

for i in range(a, b + 1):
    if num(i):
        cnt += 1

print(cnt)