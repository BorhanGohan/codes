InFile = open('GradesOutput.txt', 'r')

for EachLine in InFile:
    print(EachLine, end = '')

InFile.close()
