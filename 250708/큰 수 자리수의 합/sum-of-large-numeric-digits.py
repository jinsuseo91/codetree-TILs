a, b, c = map(int, input().split())
num = a*b*c

def max_(num):
    if num == 0:
        return 0 
    return max_(num // 10) + (num % 10)

print(max_(num))