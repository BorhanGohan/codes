Done = False
CubeRoot = 0.0
Increment = 0.0001
Epsilon = 0.01
NumOfTrials = 0
Number = 54

while abs(CubeRoot**3.0 - Number) >= Epsilon:
    CubeRoot += Increment
    NumOfTrials += 1
if abs(CubeRoot**3.0 - Number) >= Epsilon:
    print('Failed on cuberoot of', Number)
else:
    print('Cube Root of ', Number, ' is ', CubeRoot, ' after ', NumOfTrials, ' trials.')
