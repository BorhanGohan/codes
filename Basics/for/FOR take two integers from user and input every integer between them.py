s=int(input('Enter start number:'))
e=int(input('Enter end number:'))

for s in range(s,e+1,1):
    if s<e:
        print(s,end=',')
    else:
        print(s,end='')
    