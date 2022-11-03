a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
d = int(input("Enter a number:"))
e = int(input("Enter a number:"))

if c>a and c>b and c<d and c<e:
    print(f"{c} is the middle number.")
elif d>a and d>b and d<c and d<e:
    print(f"{d} is the middle number.")
elif e>a and e>b and e<d and e<c:
    print(f"{e} is the middle number.")
elif a>b and a>c and a<d and a<e:
    print(f"{a} is the middle number.")
else:
    print(f"{b} is the middle number.")
    
