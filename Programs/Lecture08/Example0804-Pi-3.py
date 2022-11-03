# Third estimate

import math

Epsilon = 1.0e-12
n = 0
NumOfTerms = 1
Term = 1.0/3.0
Sum = 1.0/3.0
while Term > Epsilon:
    n += 1
    Term = 1.0/float((4*n+1)*(4*n+3))
    Sum += Term
    NumOfTerms += 1
pi = 8*Sum
print('Calculated Value of pi: '+str(pi)+' after '+str(NumOfTerms)+' terms.')
print('Python library value  : '+str(math.pi))
