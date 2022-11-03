# Computes the Machine epsilon.

MachineEpsilon = 1.0

while 1.0 + MachineEpsilon > 1.0:
    MachineEpsilon /= 2
print('Machine Epsilon = ', MachineEpsilon)
