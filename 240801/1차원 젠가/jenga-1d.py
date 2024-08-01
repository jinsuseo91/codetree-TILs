n = int(input())
blank = 0
arr = [int(input()) for _ in range(n)]
remo = [map(int, input().split()) for _ in range(2)]

temp = [0] * n

for i in range(len(remo)):
    if i == 0:
        s1, e1 = remo[i]
        s1 -= 1
        e1 -= 1
    else:
        s2, e2 = remo[i]
        s2 -= 1
        e2 -= 1

# 제거하기
def dele(arr, s, e):
    tempRow = n-1
    for i in range(s1, e1+1):
        arr[i] =  0

    for i in range(n-1, -1, -1):
        if arr[i] != blank:
            temp[tempRow] = arr[i]
            tempRow -= 1

    return temp

arr = dele(arr, s1, e1)
arr = dele(arr, s2, e2)



a = sum(1 for x in arr if x != 0)
print(a)

for i in arr:
    if i != 0:
        print(i)