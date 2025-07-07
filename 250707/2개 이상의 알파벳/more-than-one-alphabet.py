from collections import defaultdict

a = input()
aa = defaultdict(int)
# Please write your code here.
for i in list(a):
    aa[i] += 1

if len(aa) >= 2:
    print("Yes")
else:
    print("No")