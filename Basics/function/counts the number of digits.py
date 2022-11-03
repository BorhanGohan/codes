def digits(n):
    count=0
    for i in range(n):
        if n!=0:
            n=n//10
            count+=1
    return count
n=int(input('ENTER:'))
a=digits(n)
print(a)