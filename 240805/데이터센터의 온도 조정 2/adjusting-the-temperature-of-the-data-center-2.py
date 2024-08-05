max_t=1000
n, c, g, h= list(map(int,input().split()))
ta, tb= [0]*n, [0]*n

for i in range(n):
    ta[i], tb[i] = list(map(int, input().split()))

def aa(a,b,t):
    if t < a:
        return c
    elif t <= b:
        return g
    else:
        return h
        
def bb(t):
    to = 0
    for i in range(n):
        to += aa(ta[i], tb[i], t)
    return to

max_out = 0
for t in range(max_t+1):
    max_out = max(max_out, bb(t))

print(out)