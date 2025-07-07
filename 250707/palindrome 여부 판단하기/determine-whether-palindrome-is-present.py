a = input()

def pali(a):
    if a == a[::-1]:
        print("Yes")
    else:
        print("No")
pali(a)