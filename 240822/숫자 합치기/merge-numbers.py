n = int(input())

arr = list(map(int,input().split()))

arr.sort()
cnt = 0
tot = 0
result = []

while len(arr) > 1:
    fi = arr.pop(0)
    se = arr.pop(0)
    cnt = fi + se
    tot += cnt

    arr.append(cnt)
    arr.sort()
print(tot)