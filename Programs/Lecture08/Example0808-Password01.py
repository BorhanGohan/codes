# Password validation.

Valid = False
for char in 'ToughLuck':
    if ord(char) >=65 and ord(char) <=90 or ord(char) >=97 and ord(char) <=122:
        Valid = False
    else:
        Valid = True
        break

if not Valid:
    print('Password must contain uppercase and lowercase characters,\
 and at least one special character')
else:
    print('Valid password')
