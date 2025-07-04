n = int(input())
m = int(input())

if n == 0:
    if m >= 19:
        print("MAN")
    else:
        print("BOY")
else:
    if m >= 19:
        print("WOMAN")
    else:
        print("GIRL")