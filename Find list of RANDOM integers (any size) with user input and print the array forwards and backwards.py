import random
mylist=[]
n=int(input('Enter the number of integers:'))
for i in range(0,n,1):
    i=random.randint(0,n)
    mylist.append(i)
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)