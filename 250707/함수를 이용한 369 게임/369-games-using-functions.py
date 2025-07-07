a, b = map(int, input().split())

def contain_369(n):
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True

        n //= 10
    return False

def is_369(n):
    return contain_369(n) or (n % 3 == 0)

cnt = 0

for i in range(a, b + 1):
    if is_369(i):
        cnt += 1
print(cnt)