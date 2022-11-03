import string
print("Letter from a to z=>")
for i in string.ascii_lowercase:
    if i=='z':
        print(i, end='')
    else:
        print(i, end =',')
        
print("\n\nLetter from A to Z=>")
for i in string.ascii_uppercase:
    if i=='Z':
        print(i, end='')
    else:
        print(i, end =',')
