# A program to compute the factorial of an integer.

Done = False
while not Done:
    x = float(input('Enter an integer: '))
    if float(int(x)) != float(x):
        print('Invalid entry.')
    else:
        Done = True

i = int(x)

if i >=0:
    Valid = True
else:
    Valid = False
    print('Invalid entry.')

if Valid:
    Factorial = 1
    for num in range(1,i+1):
        Factorial *= num
    print('Factorial of '+str(i)+' is '+str(Factorial))
