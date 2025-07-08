n = int(input())

arr = list(map(int, input().split()))

def find_gcd(n, m):
    gcd = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    return gcd

def find_lcm(n, m):
    return n * m // find_gcd(n, m)

def lcm_list(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]
    return find_lcm(arr[idx], lcm_list(arr, idx + 1))

print(lcm_list(arr, 0))