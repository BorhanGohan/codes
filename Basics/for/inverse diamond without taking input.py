
for i in range(1,5,1):
    for j in range(1,i,1):
        print(' ',end='')
    for j in range(1,7-i,1):
        print('*',end='')
    for j in range(1,6-i,1):
        print('*',end='')
    print()
for i in range(1,6,1):
    for j in range(1,6-i,1):
        print(' ',end='')
    for j in range(1,i+1,1):
        print('*',end='')
    for j in range(1,i,1):
        print('*',end='')
    print()

