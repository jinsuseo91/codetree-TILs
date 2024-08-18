from itertools import combinations

n, m = map(int, input().split())
data = []
for i in range(1, n+1):
    data.append(i)


result= list(combinations(data, m))
for i in result:
    print(*i)