i = input()
i = i [::-1]

for char in i.lower():
    print(ord(char)-ord('a')+1, end=" ")