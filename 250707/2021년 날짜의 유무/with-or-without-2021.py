m, d = map(int, input().split())

def calendar(m, d):
    if m in [1,3,5,7,8,10,12]:
        if d < 32:
            return True
        else:
            return False
    elif m == 2:
        if d > 28:
            return False
        else:
            return True
    else:
        if d < 31:
            return True
        else:
            return False
if calendar(m, d):
    print('Yes')
else:
    print('No')