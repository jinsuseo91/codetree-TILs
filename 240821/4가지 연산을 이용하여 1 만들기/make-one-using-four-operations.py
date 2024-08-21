from collections import deque

n = int(input())
q = deque()

q.append((n, 0))
visited = [n]
answer = 0

def bfs():
    global answer
    while q:
        now_, t = q.popleft()
        if now_ == 1:
            answer = t
            return 

        if now_ // 3 not in visited and now_ % 3 == 0:
            visited.append(now_//3)
            q.append((now_ // 3, t + 1))
        if now_ // 2 not in visited and now_ % 2 == 0:
            visited.append(now_//2)
            q.append((now_ // 2, t + 1))
        if now_ - 1 not in visited:
            visited.append(now_-1)
            q.append((now_ - 1, t + 1))
        if now_ + 1 not in visited:
            visited.append(now_+1)
            q.append((now_ + 1, t + 1))

bfs()
print(answer)