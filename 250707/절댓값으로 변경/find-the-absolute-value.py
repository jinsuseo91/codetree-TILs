n = int(input())
arr = list(map(int, input().split()))
arr2 = []
# Please write your code here.
def func(arr):
    for i in arr:
        if i < 0:
            i = -i
        arr2.append(i)
func(arr)
for i in arr2:
    print(i, end=' ')