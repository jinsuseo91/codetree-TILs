y, m, d = map(int, input().split())

# Please write your code here.
def calendar(y, m, d):
    if year_4(y):
        if m in [1,3,5,7,8,10,12]:
            if d > 31:
                return False
            if m in [3,5]:
                return 'Spring'
            elif m in [7, 8]:
                return 'Summer'
            elif m == 10:
                return 'Fall'
            elif m in [1, 12]:
                return 'Winter'
        elif m in [4,6,9,11]:
            if d > 30:
                return False
            if m == 4:
                return 'Spring'
            elif m == 6:
                return 'Summer'
            elif m in [9, 11]:
                return 'Fall'
        elif m == 2:
            if d > 29:
                return False
            return 'Winter'
    else:
        if m in [1,3,5,7,8,10,12]:
            if d > 31:
                return False
            if m in [3,5]:
                return 'Spring'
            elif m in [7, 8]:
                return 'Summer'
            elif m == 10:
                return 'Fall'
            elif m in [1, 12]:
                return 'Winter'
        elif m in [4,6,9,11]:
            if d > 30:
                return False
            if m == 4:
                return 'Spring'
            elif m == 6:
                return 'Summer'
            elif m in [9, 11]:
                return 'Fall'
        elif m == 2:
            if d > 28:
                return False
            return 'Winter'

def year_4(y):
    if y % 4 != 0:
        return False
    if y % 100 != 0:
        return True
    if y % 400 == 0:
        return True
    return False

if calendar(y, m, d) == False:
    print(-1)
else:
    print(calendar(y,m,d))