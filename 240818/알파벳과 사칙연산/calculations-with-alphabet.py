n = list(input())

alpha = []
math = []

for e in n:
    if e.isalpha():
        alpha.append(e)
    else:
        math.append(e)

unique_alpha = list(set(alpha))
alpha_mapping = {a: 0 for a in unique_alpha}
memo = {}

def compute():

    for i, k in enumerate(unique_alpha):
        alpha_mapping[k] = selected[i]
    
    r = alpha_mapping[alpha[0]]

    for i, ex in enumerate(math):
        a = alpha[i + 1]
        if ex == "-":
            r -= alpha_mapping[a]
        elif ex == "+":
            r += alpha_mapping[a]
        elif ex == "*":
            r *= alpha_mapping[a]

    return r

def check(idx):
    global result
    key = tuple(selected)
    if key in memo:
        return memo[key]

    if idx == len(unique_alpha):
        val = compute()
        result = max(result, val)
        memo[key] = val
        return

    for i in range(1, 5):
        selected.append(i)
        check(idx + 1)
        selected.pop()

result = float('-inf')
selected = []
check(0)

print(result)