n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

cnt = 0
def dfs(v):
    global cnt
    for curr_v in range(1, n + 1):
        if graph[v][curr_v] and not visited[curr_v]:
            cnt += 1
            visited[curr_v]= True
            dfs(curr_v)
    return cnt

for i in range(m):
    p1, p2 = map(int, input().split())
    graph[p1][p2] = 1
    graph[p2][p1] = 1

root_v = 1
visited[root_v] = True
ans = dfs(root_v)
print(ans)