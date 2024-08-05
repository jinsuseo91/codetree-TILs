n = int(input())
arr = []
ans = []
cnt = 0

def choose(curr_num):
    global cnt
    if curr_num == n + 1:
        cnt += beauty()
        return
    
    for i in range(1, 5):
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

def beauty():
    i = 0
    while i < n:
        if i + arr[i] - 1 >= n:
            return 0
        
        for j in range(i, i + arr[i]):
            if arr[j] != arr[i]:
                return 0
        i += arr[i]
    return 1

choose(1)
print(cnt)