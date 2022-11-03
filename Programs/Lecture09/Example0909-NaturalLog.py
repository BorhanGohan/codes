# Series to compute natural logarithm.

import math

Epsilon = 1.0e-17

x = float(input('Enter a positive number (>0): '))

if x > 0:
    Fraction = (x - 1)/(x + 1)
    Term = Fraction
    Sum = Term
    n = 1
    while Term > Epsilon:
        n +=2
        Term = Term*Fraction**2
        Sum +=Term/n
    NaturalLog = 2.0*Sum
    print('Calculated logarithm:', NaturalLog)
    print('Library logarithm   :', math.log(x))
        
