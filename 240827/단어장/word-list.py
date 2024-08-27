from sortedcontainers import SortedDict

n = int(input())
arr = [input() for _ in range(n)]
d = SortedDict()

for word in arr:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

for word, cnt in d.items():
    print(word, cnt)