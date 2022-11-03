Done = False
CubeRoot = 0.0
Increment = 0.0001
Epsilon = 0.001
NumOfTrials = 0
Number = 54

while not Done:
    Difference = abs(CubeRoot**3.0 - Number)
    if Difference < Epsilon:
        Done = True
        break
    else:
        CubeRoot += Increment
        NumOfTrials += 1
if abs(CubeRoot**3.0 - Number) >= Epsilon:
    print('Failed on cuberoot of', Number)
else:
    print('Cube Root of ', Number, ' is ', CubeRoot, ' after ', NumOfTrials, ' trials.')
