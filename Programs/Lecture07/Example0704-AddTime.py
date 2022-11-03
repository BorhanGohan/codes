# The program adds two time entities.
# Hour, minute and seconds are read for each time.

# Input the first time

FirstTimeValid = True

FirstHour = float(input('Enter first hour  : '))
FirstMinute = float(input('Enter first minute: '))
FirstSecond = float(input('Enter first second: '))

# Check for validity of first time input

if FirstHour < 0:
    FirstTimeValid = False

if FirstMinute < 0 or FirstMinute > 60:
    FirstTimeValid = False

if FirstSecond < 0 or FirstSecond > 60:
    FirstTimeValid = False

print()

# Input the second time

SecondTimeValid = True

SecondHour = float(input('Enter second hour  : '))
SecondMinute = float(input('Enter second minute: '))
SecondSecond = float(input('Enter second second: '))

# Check for validity of second time input

if SecondHour < 0:
    SecondTimeValid = False

if SecondMinute < 0 or FirstMinute > 60:
    SecondTimeValid = False

if FirstSecond < 0 or FirstSecond > 60:
    SecondTimeValid = False

print()

# If invalid input, report

if not FirstTimeValid:
    print('Invalid input for first time.')

if not SecondTimeValid:
    print('Invalid input for second time.')

# If inputs are valid, add time and print result

if FirstTimeValid and SecondTimeValid:
    TotalHour = FirstHour + SecondHour
    TotalMinute = FirstMinute + SecondMinute
    TotalSecond = FirstSecond + SecondSecond
    
    if TotalSecond >= 60:
        TotalSecond -= 60
        TotalMinute += 1

    if TotalMinute >=60:
        TotalMinute -=60
        TotalHour += 1

    print('Total time: '+str(int(TotalHour))+' hours, '+str(int(TotalMinute))\
          +' minutes, '+str(int(TotalSecond))+' seconds.')
