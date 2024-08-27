from sortedcontainers import SortedDict
n = int(input())
arr = list(map(int, input().split()))
d = SortedDict()

for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = i + 1

for num, cnt in d.items():
    print(num, cnt)