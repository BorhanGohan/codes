import random
mylist=[]
for i in range(11):
    n=random.randint(0,11)
    mylist.append(n)
# for i in mylist:
    print(n,end=',')
print()
for i in range (len(mylist)):
    for j in range(len(mylist)-i-1):
        if mylist[j]>mylist[j+1]:
            temp=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp
print(mylist)
print()

print('first min:',mylist[0])
print('second min:',mylist[1])
print('first max:',mylist[len(mylist)-1])
print('second max:',mylist[len(mylist)-2])
print('median:',mylist[len(mylist)//2])