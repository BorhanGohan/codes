# Second estimate

import math

Epsilon = 1.0e-12
n = 1
NumOfTerms = 1
s = 1
Term = 1.0
Sum = 1.0
while Term > Epsilon:
    n += 1
    s = -s
    Term = 1.0/float(n*n)
    Sum += s*Term
    NumOfTerms += 1
pi = (12*Sum)**0.5
print('Calculated Value of pi: '+str(pi)+' after '+str(NumOfTerms)+' terms.')
print('Python library value  : '+str(math.pi))
