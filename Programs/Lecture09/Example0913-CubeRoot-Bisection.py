# Cube root. Bisection search

x = float(input('Enter a number: '))
Epsilon = 1.0e-13
NumOfTrials = 0
LowGuess = 1.0
HighGuess = x
Estimate = (HighGuess + LowGuess)/2.0
Done = False

while not Done:
    NumOfTrials += 1
    Difference = abs(Estimate**3 - x)
    if Difference <= Epsilon or abs(Estimate - LowGuess) <= Epsilon:
        Done = True
        break
    if Estimate**3 < x:
        LowGuess = Estimate
    else:
        HighGuess = Estimate
    Estimate = (HighGuess + LowGuess)/2.0
print('Cube root of ', x, ' is ', Estimate)
print('Number of trials needed: ', NumOfTrials)
print('Cube of Estamate: ', Estimate*Estimate*Estimate)
