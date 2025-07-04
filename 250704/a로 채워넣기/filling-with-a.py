string = input()
leng = len(string)

string = string[:1] + 'a' + string[2:]
string = string[:leng - 2] + 'a' + string[leng - 1:]

print(string)