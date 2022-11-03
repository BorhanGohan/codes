a=float(input('Enter a:'))
b=float(input('Enter b:'))
c=float(input('Enter c:'))

if a**2==b**2+c**2:
    print('Right triangle')
elif b**2==a**2+c**2:
    print('Right triangle')
elif c**2==b**2+a**2:
    print('Right triangle')
else:
    print('Not a right triangle')
    
    