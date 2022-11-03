import random
mylist=[0]
n=int(input('Enter the size of list:'))
for i in range(0,n,1):
    num=random.randint(20,40)
    mylist.append(num)
    print(num,end=',')
print()
x=int(input('Enter a number to search in list:'))
found=False
for i in mylist:
    if x==i:
        found=True
if found==True:
    print('Value is found')
else:
    print('Value not found')