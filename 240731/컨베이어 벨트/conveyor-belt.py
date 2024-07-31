n, t = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
array = array1 + array2
# for i in range(2*n):
for j in range(t):
    temp = array[2*n-1]
    for k in range(2*n-1, 0, -1):
        array[k] = array[k-1]
    array[0] = temp
print(*array[0:n])
print(*array[n:2*n])