num=[]
a=True
b=True
for i in range(5):
    n=int(input('enter:'))
    num.append(n)
print(num)
for i in range(len(num)-1):
    if i==len(num)-1:
        break
    if num[i]<num[i+1]:
        a=False
    i=i+1
for i in range(len(num)-1):
    if i==len(num):
        break
    if num[i]>num[i+1]:
        b = False
    i=i+1
if a==True:
    print ("Yes, List is sorted. It is in descending form.")
elif b==True:
    print ("Yes, List is sorted. It is in ascending form.")
else:
    print('not sorted')