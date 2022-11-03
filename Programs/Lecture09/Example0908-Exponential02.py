import math

MachineEpsilon = 1.0

while 1.0 + MachineEpsilon > 1.0:
    MachineEpsilon /= 2

NewTerm = 1.0
Expo = 1.0
OldTerm = 1.0
n = 0

while NewTerm > MachineEpsilon:
    n += 1
    NewTerm = OldTerm/float(n)
    Expo = Expo + NewTerm
    OldTerm = NewTerm

x = float(input('Enter the value of x: '))

Negative = False
if x < 0:
    Negative = True
    x = -x

w = int(x)
f = x - w

ew = 1
for i in range(1,w+1):
    ew *= Expo

NewTerm = f
Expof = 1.0
OldTerm = 1.0
n = 0

while NewTerm > MachineEpsilon:
    n += 1
    NewTerm = OldTerm*f/float(n)
    Expof = Expof + NewTerm
    OldTerm = NewTerm

ExpoX = ew*Expof

if Negative:
    ExpoX = 1.0/ExpoX
    x = -x

print('Calculated exponential: ', ExpoX)
print('From math module      : ', math.exp(x))



