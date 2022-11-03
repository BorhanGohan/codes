# Demonstrates break and continue statements

# break statement

# Grades of 10 students have been submitted.

for Grades in ('B', 'C', 'A', 'B', 'C', 'A', 'Z', 'D', 'B', 'C'):
    if Grades == 'Z':
        print("You must submit all grades. Cannot leave a 'Z' grade on record")
        print('All grades ignored.')
        print()
        break
    print('Grades '+Grades+ ' has been received and will be recorded')
    input()
    print()

input('Press ENTER to continue')

# continue statement

# Grades of 10 students have been submitted.

for Grades in ('B', 'C', 'A', 'B', 'C', 'A', 'W', 'D', 'B', 'C'):
    if Grades == 'W':
        print('Grade '+Grades+' has been recorded, and will not be used in calculation.')
        input()
        print()
        continue
    print('Grade '+Grades+' has been recorded, and will be used in calculation.')
    input()
    print()
