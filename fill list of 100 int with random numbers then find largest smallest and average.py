import random
mylist=[]
for i in range(0,100):
    num=random.randint(0,100)
    mylist.append(num)
for i in mylist:
    print(i,end=',')
    
largest=mylist[0]
smallest=mylist[0]
for i in mylist:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
average=num/len(mylist)
print('\naverage:',average)
print('largest:',largest)
print('smallest:',smallest)
