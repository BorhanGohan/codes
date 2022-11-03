# Square root. Herion of Alexanderia.

x = float(input('Enter a number: '))

Guess = x/2
Done = False
Epsilon = 1.0e-17
NumOfTrials = 0

while not Done:
    Difference = abs(Guess**2.0 - x)
    if Difference < Epsilon:
        Done = True
    NewGuess = (Guess + x/Guess)/2.0
    NumOfTrials += 1
    Guess = NewGuess
print('Square root of ', x, 'is ', Guess)
print('Number of trials needed: ', NumOfTrials)
