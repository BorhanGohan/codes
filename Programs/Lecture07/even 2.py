x=float(input('Enter a number:'))
WholeNumber= False
if float(int(x))==x:
    WholeNumber=True
else:
    print('Please enter a whole number.')

if WholeNumber:
    if x%2==0:
        print('The number '+str(x)+' is an even number')
    else:
        print ('The number '+str(x)+' is not an even number')
                    
