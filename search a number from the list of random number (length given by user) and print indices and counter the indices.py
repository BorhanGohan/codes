import random
mylist=[]
n=int(input('Enter the size of list:'))
for i in range(0,n,1):
    num=random.randint(20,40)
    mylist.append(num)
for i in mylist:
    print(i,end=',')
print()
x=int(input('Enter a number to search in list:'))
indices=[]
found=False
for i in mylist:
    if x==i:
        found=True
if found==True:
    print('Value is found')
else:
    print('Value not found')
counter=0
for i in range(len(mylist)):
    if x==mylist[i]:
        counter+=1
#     counter=mylist.count(x)
#     if x==mylist[i]:
        indices.append(i)
for i in indices:
    print(i,end=',')
print()
print('Totals indices:',counter)