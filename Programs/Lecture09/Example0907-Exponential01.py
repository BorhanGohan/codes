import math

MachineEpsilon = 1.0

while 1.0 + MachineEpsilon > 1.0:
    MachineEpsilon /= 2
print('MachineEpsilon = ', MachineEpsilon)

NewTerm = 1.0
Expo = 1.0
OldTerm = 1.0
n = 0

while NewTerm > MachineEpsilon:
    n += 1
    NewTerm = OldTerm/float(n)
    Expo = Expo + NewTerm
    OldTerm = NewTerm
print('e = ', Expo, ' after ', n, ' terms.')
print(math.exp(1))

