n = int(input())
blank = 0
arr = [int(input()) for _ in range(n)]
remo = [map(int, input().split()) for _ in range(2)]

tempRow = n-1
# 제거하기
def dele(arr, s, e):
    s -= 1
    e -= 1

    for i in range(s, e + 1):
        arr[i] =  0
    
    temp = [x for x in arr if x != 0]

    return temp

s1, e1 = remo[0]
arr = dele(arr, s1, e1)

s2, e2 = remo[1]
arr = dele(arr, s2, e2)

print(len(arr))

for i in arr:
    print(i)