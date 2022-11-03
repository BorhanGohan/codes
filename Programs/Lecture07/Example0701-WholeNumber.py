# The program checks if a number that has been entered is a whole number.

x = float(input('Enter a number: '))

if float(int(x)) == x:
    print('The number '+str(x)+' is a whole number.')
else:
    print('The number '+str(x)+' is a not whole number.')
