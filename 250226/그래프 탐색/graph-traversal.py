n, m = tuple(map(int, input().split()))
visited = [False] * n
arr = [[] for _ in range(n + 1)]
result = 0

for _ in range(m):
    s, e = tuple(map(int, input().split()))
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