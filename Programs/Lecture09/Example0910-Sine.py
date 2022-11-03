# Finds the sine of an angle.

import math

# We will use the values of Machine Epsilon and pi from earlier programs.

MachineEpsilon = 1.1102230246251565e-16

pi = 3.1415926535897922

Angle = float(input('Enter an angle (in radians): '))

# Remove multiples of 2*pi from Angle

i = int(Angle/(2*pi))

x = Angle - 2*i*pi

# Determine the quadrant of the angle

i = int(2*x/pi) + 1

if i == 1:
    Quadrant = 1
    x = x
elif i == 2:
    Quadrant = 2
    x = pi - x
elif i == 3:
    Quadrant = 3
    x = x - pi
elif i == 4:
    Quadrant = 4
    x = x

OldTerm = x
Sine = OldTerm
n = 1
s = 1
while abs(OldTerm) > MachineEpsilon:
    n +=2
    s = -s
    NewTerm = OldTerm*x*x/((n - 1)*n)
    Sine += s*NewTerm
    OldTerm = NewTerm

if Quadrant == 3 or Quadrant == 4:
    Sine = -Sine

print('Sine of '+str(Angle)+' radians is: '+str(Sine))
print('From library function, Sin(Angle):'+str(math.sin(Angle)))
