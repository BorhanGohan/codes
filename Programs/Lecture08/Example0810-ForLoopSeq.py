# Demonstration of for loop with a sequence of data.

# These are 10 marks received by 10 students in a class.

MinMarks = 100
MaxMarks = 0
Sum = 0
for Marks in (60, 40, 80, 90, 89, 78, 76, 95, 69, 56):
    Sum += Marks
    if Marks > MaxMarks:
        MaxMarks = Marks
    if Marks < MinMarks:
        MinMarks = Marks
Mean = Sum/10
print('Class average = ',format(Mean,'5.2f'))
print('Class maximum = ',format(MaxMarks,'5.2f'))
print('Class minimum = ',format(MinMarks,'5.2f'))
