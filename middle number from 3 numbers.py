a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
if a==b or b==c or a==c:
    print("There is no middle number.")
elif a>c and a<b:
    print(f"{a} is the middle number.")
elif b>a and b<c:
    print(f"{b} is the middle number.")
else:
    print(f"{c} is the middle number.")