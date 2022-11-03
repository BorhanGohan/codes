a =int(input("Enter the number1: "))
b =int(input("Enter the number2: "))
c =int(input("Enter the number3: "))
d =int(input("Enter the number4: "))
if a>b:
    if a>c:
        if a>d:
            print(f"{a} is largest")
        else :
            print(f"{d} is largest")
    elif c>d:
                print(f"{c} is largest")
    else:
             print(f"{d} is largest")
                    
else:
    if b>c:
        if b>d:
            print(f"{b} is largest")
        else :
            print(f"{d} is largest")
    elif c>d:
                print(f"{c} is largest")
    else:
             print(f"{d} is largest")