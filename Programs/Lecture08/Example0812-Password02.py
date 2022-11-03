# Password entry validation.

Valid = False
LengthValid = False
UpperCase = False
LowerCase = False
Digits = False
SpecChar = False

while not Valid:
    print('Enter your password. Please follow the following guidelines.')
    print('(a) At least 12 chacters long.')
    print('(b) Must contain both uppercase and lowercase letters.')
    print('(c) Must contain at least one number digit.')
    print('(d) Must contain at least one special character (!@#$%&): ')
    print()
    PassWord = input('Enter a password: ')

    if len(PassWord) >= 12:
        LengthValid = True

    PassLen = len(PassWord)

    for i in range(PassLen):
        if ord(PassWord[i]) >= 65 and ord(PassWord[i]) <= 90:
            UpperCase = True
        if ord(PassWord[i]) >= 97 and ord(PassWord[i]) <= 122:
            LowerCase = True
        if ord(PassWord[i]) >= 48 and ord(PassWord[i]) <= 57:
            Digits = True
        if ord(PassWord[i]) == 33 or ord(PassWord[i]) == 64 or \
            ord(PassWord[i]) == 35 or ord(PassWord[i]) == 36 or \
            ord(PassWord[i]) == 37 or ord(PassWord[i]) == 38 :
            SpecChar = True

    if LengthValid and UpperCase and LowerCase and Digits and SpecChar :
        Valid = True
    else:
        print()
        print('Invalid Entry. Enter again.')
        print()
        LengthValid = False
        UpperCase = False
        LowerCase = False
        Digits = False
        SpecChar = False

                
