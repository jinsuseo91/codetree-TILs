from sortedcontainers import SortedDict

n = int(input())
d = SortedDict()

arr = [input() for _ in range(n)]

for word in arr:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

for word, cnt in d.items():
    ratio = cnt / n * 100

    print(f"{word} {ratio:.4f}")