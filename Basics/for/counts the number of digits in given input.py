n=int(input("Enter a number:"))
counter=0
for i in range(n):
    if n!=0:
        n=n//10
        counter+=1
print('Number of digits:',counter)