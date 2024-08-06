n, m = map(int, input().split())

ans = []

def print_answer():
    for i in ans:
        print(i, end=' ')
    print()

def choose(curr_num, num):
    if curr_num == m + 1:
        print_answer()
        return
    
    for i in range(1, n + 1):
        if i > num:
            ans.append(i)
            choose(curr_num + 1, i)
            ans.pop()

choose(1,0)