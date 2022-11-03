InFile = open('e:/csc101/20341950.dat', 'r')

InFile.readline()

Year = []
AnnualTemp = []
MonthlyTemp = []

for EachLine in InFile:
    Year.append(EachLine[11:15])
    for i in range(20,108,8):
        MonthlyTemp.append(int(EachLine[i:i+4]))
    YearSum = 0
    for Temp in MonthlyTemp:
        YearSum += Temp
    AnnualTemp.append(YearSum/12/100)
    MonthlyTemp.clear()

InFile.close()

OutFile = open('Barishal.dat', 'w')

for i in range(0,len(Year)):
    print('{:>4}'.format(Year[i]),'{:>5.2f}'.format(AnnualTemp[i]), file = OutFile)

OutFile.close()
