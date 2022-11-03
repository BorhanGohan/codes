i = 0
sum = 0
for i in range(1,1025,1):
    n = 2**i
    sum = sum + n
    if n<1024:
        print(n,end="+")
    elif n==1024:
        print(n,end="=")
        print(sum)