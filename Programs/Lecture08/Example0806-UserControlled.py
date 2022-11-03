# User-controlled while-loop

Done = False

while not Done:
    IDNum = input('Enter ID Number: ')
    Name = input('Enter a name: ')
    Age = input('Enter Age: ')
    print(IDNum, Name, Age)
    Response = input('Do you want to continue? [Y/N]')
    if Response.upper() != 'Y':
        Done = True
