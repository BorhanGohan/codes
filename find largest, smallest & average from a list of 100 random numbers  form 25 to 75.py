import random
# for i in range(0,25):
#     i=random.randint(25,100)
#     print(i ,end=' ')
mylist=[]
for i in range(0,100):
    num=random.randint(25,75)
    mylist.append(num)
print(mylist)
largest=mylist[0]
smallest=mylist[0]
for i in mylist:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
        average=num/len(mylist)
print('average:',average)
print('largest:',largest)
print('smallest:',smallest)