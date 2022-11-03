start=int(input('Enter start number:'))
end=int(input('Enter end number:'))
sum=0
for start in range(start,end+1,1):
    if start%2!=0:
        print(start,end=',')
        sum=sum+start
print('\nThe sum is', sum)