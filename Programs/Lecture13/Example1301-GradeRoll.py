Student = []

Student.append([('921-09-3421', 'Abdul Wahab'), [90, 98, 85, 88, 76]])
Student.append([('785-87-2356', 'Faisal Mahmud'), [78, 76, 60, 76, 60]])
Student.append([('455-98-3244', 'Sanjida Khanam'), [76, 88, 79, 80, 70]])
Student.append([('876-78-3457', 'Alpona Kasem'), [76, 65, 89, 78, 90]])
Student.append([('457-08-9698', 'Ahmed Salah'), [54, 67, 56, 69, 66]])
Student.append([('654-35-3242', 'Kabir Mohammad'), [65, 74, 50, 45, 70]])
Student.append([('897-09-8547', 'Samina Ashraf'), [90, 95, 80, 85, 90]])

# Find the maximum of each test.

for TestIndex in range(5):
    TestMax = 0
    for StudIndex in range(7):
        if Student[StudIndex][1][TestIndex] > TestMax:
            TestMax = Student[StudIndex][1][TestIndex]
            MaxLoc = StudIndex
    print('Maximum of Test '+str(TestIndex+1)+': '+str(TestMax)+' by '+Student[MaxLoc][0][1])

print()
input('Press ENTER to Continue')
print()

# Find the minimum of each test.

for TestIndex in range(5):
    TestMin = 100
    for StudIndex in range(7):
        if Student[StudIndex][1][TestIndex] < TestMin:
            TestMin = Student[StudIndex][1][TestIndex]
            MinLoc = StudIndex
    print('Minimum of Test '+str(TestIndex+1)+': '+str(TestMin)+' by '+Student[MinLoc][0][1])

print()
input('Press ENTER to Continue')
print()

# Finds the average of each test.

for TestIndex in range(5):
    TestTot = 0
    for StudIndex in range(7):
        TestTot += Student[StudIndex][1][TestIndex]
    TestAve = TestTot/7
    print('Average of Test '+str(TestIndex+1)+': ','{:>5.1f}'.format(TestAve))

print()
input('Press ENTER to Continue')
print()

# Finds the final grade.

OutFile = open('GradesOutput.txt', 'w')

print('Student ID   Student Name      Total  Percent  Grade', file=OutFile)
print('----------   ------------      -----  -------  -----', file=OutFile)

for StudIndex in range(7):
    TestTot = 0
    for TestIndex in range(5):
        TestTot +=Student[StudIndex][1][TestIndex]
    TotPercent = TestTot/500*100
    if TotPercent >=85:
        FinalGrade = 'A'
    elif TotPercent >=70:
        FinalGrade = 'B'
    elif TotPercent >=55:
        FinalGrade = 'C'
    elif TotPercent >=40:
        FinalGrade = 'D'
    else:
        FinalGrade = 'F'
    print('{:<12}'.format(Student[StudIndex][0][0]),\
          '{:<15}'.format(Student[StudIndex][0][1]),\
          '{:>6}'.format(TestTot),'{:>8.2f}'.format(TotPercent),\
          '{:>5}'.format(FinalGrade), file=OutFile)
OutFile.close()

