num=int(input())
rev=0
while num!=0:
    r=num%10
    num=num//10
    rev=r+rev*10
print(rev)