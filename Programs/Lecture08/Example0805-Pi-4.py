# Fourth estimate

import math

Epsilon = 1.0e-16
n = 0
NumOfTerms = 1

Term = 1.0
Sum = 1.0
while Term > Epsilon:
    n += 1
    Term = (2**n)*(math.factorial(n)**2)/(math.factorial(2*n+1))
    Sum += Term
    NumOfTerms += 1
pi = 2*Sum
print('Calculated Value of pi: '+str(pi)+' after '+str(NumOfTerms)+' terms.')
print('Python library value  : '+str(math.pi))
