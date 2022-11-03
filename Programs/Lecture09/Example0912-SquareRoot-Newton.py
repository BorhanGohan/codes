# Square root - Newton-Raphson

x = float(input('Enter a number: '))

OldGuess = x/2
Epsilon = 1.0e-17
NumOfIter = 0
Done = False

while not Done:
    NumOfIter += 1
    NewGuess = OldGuess - (OldGuess**2.0 - x)/(2.0*OldGuess)
    if abs(OldGuess - NewGuess) < Epsilon:
        Done = True
    else:
        OldGuess = NewGuess
print('Square root of ', x, 'is ', NewGuess)
print('Number of interations needed: ', NumOfIter)
print('Square of the result: ', NewGuess*NewGuess)
