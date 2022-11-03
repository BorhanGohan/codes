# Finds roots of a quadratic equation

import math

a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))

D = b*b - 4*a*c

print()
print('D='+str(D))

if D>0:
    print('Real roots')
    FirstRoot=(-b+math.sqrt(D))/(2*a)
    SecondRoot=(-b-math.sqrt(D))/(2*a)
    print('First Root ='+str(format(f'{FirstRoot}')))
    print('Second Root='+str(format(f'{SecondRoot}')))
elif D==0:
    print('Equal roots')
    Root=-b/(2*a)
    print('Root='f'{Root}')
else:
    print('Complex roots')
    RealPart=-b/(2*a)
    ImagPart=math.sqrt(-D)
    print('First Root ='+str(format(f'{RealPart}'))+'+i' \
          +str(f'{ImagPart}'))
    print('Second Root ='+str(format(f'{RealPart}'))+'-i' \
          +str(f'{ImagPart}'))
# a=float(input("Enter a number"))
# b=float(input("Enter a number"))
# c=float(input("Enter a number"))
# x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
# print(x1)
# x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
# print(x2)