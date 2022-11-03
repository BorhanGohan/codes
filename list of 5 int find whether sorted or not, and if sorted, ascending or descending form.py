num = [5,4,3,3,3,2,1]   
a= True
b=True
for i in range(len(num)):
    if i==len(num)-1:
        break
    if num[i] < num[i+1]:
        a = False
for i in range(len(num)-1):
    if i==len(num):
        break
    if num[i] > num[i+1]:
        b = False
if a==True:
    print ("Yes, List is sorted. It is in descending form.")
elif b==True:
    print ("Yes, List is sorted. It is in ascending form.")
else:
    print('not sorted')