# The program takes as input four test points, their total points
# and their percentage in the final grade. It calculates the
# final points, and a final letter grade.
#
# Demonstrates if-elif-else block


# First test
FirstPoint = float(input('Points obtained in the first test: '))
FirstTotal = float(input('Total points of the first test   : '))
FirstPercent = float(input('Percentage of the first test     : '))

print()

# Second test
SecondPoint = float(input('Points obtained in the second test: '))
SecondTotal = float(input('Total points of the second test   : '))
SecondPercent = float(input('Percentage of the second test     : '))

print()

# Third test
ThirdPoint = float(input('Points obtained in the third test: '))
ThirdTotal = float(input('Total points of the third test   : '))
ThirdPercent = float(input('Percentage of the third test     : '))

print()

# Fourth test
FourthPoint = float(input('Points obtained in the fourth test: '))
FourthTotal = float(input('Total points of the fourth test   : '))
FourthPercent = float(input('Percentage of the fourth test     : '))

FinalPoint = FirstPoint/FirstTotal*FirstPercent + \
             SecondPoint/SecondTotal*SecondPercent + \
             ThirdPoint/ThirdTotal*ThirdPercent + \
             FourthPoint/FourthTotal*FourthPercent

if FinalPoint >= 90:
    FinalGrade = 'A'
elif FinalPoint >= 75:
    FinalGrade = 'B'
elif FinalPoint >= 60:
    FinalGrade = 'C'
elif FinalPoint >= 45:
    FinalGrade = 'D'
else:
    FinalGrade = 'F'

print()

print('Final point is: '+str(FinalPoint)+', Final garde is: '+str(FinalGrade))

