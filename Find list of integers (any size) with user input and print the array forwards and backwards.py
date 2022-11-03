mylist=[]
n=int(input('Enter the number of integers:'))
for i in range(0,n,1):
    mylist.append(i)
# mylist.sort()
# print(mylist)
# mylist.reverse()
# print(mylist)
for i in range (len(mylist)):
    for j in range(len(mylist)-i-1):
        if mylist[j]>mylist[j+1]:
            temp=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp
print(mylist)
print()
for i in range (len(mylist)):
    for j in range(len(mylist)-i-1):
        if mylist[j]<mylist[j+1]:
            temp=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp
print(mylist)