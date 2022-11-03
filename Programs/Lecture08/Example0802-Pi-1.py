# First estimate. Leibnitz formula for pi.

import math

Epsilon = 0.00000001
n = 1
NumOfTerms = 1
s = 1
Term = 1.0
Sum = 1.0
while Term > Epsilon:
    n += 2
    s = -s
    Term = 1.0/float(n)
    Sum += s*Term
    NumOfTerms += 1
pi = (4*Sum)
print('Calculated Value of pi: '+str(pi)+' after '+str(NumOfTerms)+' terms.')
print('Python library value  : '+str(math.pi))
