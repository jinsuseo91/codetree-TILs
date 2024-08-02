n = input()
arr = []
cnt = 0
for i in range(len(n)):
    if n[i] == "(":
        for j in range(i+1, len(n)):
            if n[j] == ")":
                cnt += 1
    else:
        continue
print(cnt)