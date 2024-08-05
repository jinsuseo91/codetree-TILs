k, n = map(int, input().split())
k += 1
arr = []

def print_answer():
    for elem in arr:
        print(elem, end =' ')
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return

    for i in range(1, k):
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()
    
    return

choose(1)