import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int, input().split())
visited = [False] * n
arr = [[] for _ in range(n + 1)]
result = 0

for _ in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

def dfs(v):   
    global result
    for i in arr[v]:
        if not visited[i]:
            visited[i] = True
            result += 1
            dfs(i)

visited[1] = True
dfs(1)
print(result)