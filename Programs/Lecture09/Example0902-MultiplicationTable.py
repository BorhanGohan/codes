# Constructs multiplication table

for k in range(2):
    for i in range(1,11):
        for j in range(5*k+1,5*k+6):
            print(format(j,'2d'),'x',format(i,'2d'),'=',format(j*i,'3d'),end='   ')
        print()
    input()
    print()
