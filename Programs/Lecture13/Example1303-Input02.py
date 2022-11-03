InFile = open('GradesOutput.txt', 'r')

for i in range(2):
    InFile.readline()

Total = []
Grade = []

for EachLine in InFile:
    Total.append(int(EachLine[32:35]))
    Grade.append(EachLine[49:50])

InFile.close()

SumTot = 0

for i in Total:
    SumTot += i

ClassAve = SumTot/len(Total)

TotGrade = [0, 0, 0, 0, 0]

for i in Grade:
    if i == 'A':
        TotGrade[0] += 1
    elif i == 'B':
        TotGrade[1] += 1
    elif i == 'C':
        TotGrade[2] += 1
    elif i == 'D':
        TotGrade[3] += 1
    elif i == 'F':
        TotGrade[4] += 1

print('Number of A: ',TotGrade[0])
print('Number of B: ',TotGrade[1])
print('Number of C: ',TotGrade[2])
print('Number of D: ',TotGrade[3])
print('Number of F: ',TotGrade[4])
print()
print('Class Average: ', '{:>5.2f}'.format(ClassAve))
