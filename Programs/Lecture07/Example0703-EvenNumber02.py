# The program will input a number. If the number is a whole
# number, it will check if the number is odd or even.

x = float(input('Enter a number: '))

WholeNumber = False

if float(int(x)) == x:
    WholeNumber = True
else:
    print('Please enter a whole number.')

if WholeNumber:
    if x%2 == 0:
        print('The number '+str(x)+' is an even number')
    else:
        print('The number '+str(x)+' is an odd number')
