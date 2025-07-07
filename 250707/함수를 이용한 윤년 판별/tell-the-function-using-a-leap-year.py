y = int(input())

# Please write your code here.
def func(y):
    if y % 4 != 0:
        return False

    if y % 100 != 0:
        return True

    if y % 400 == 0:
        return True
    
    return False

if func(y):
    print("true")
else:
    print('false')