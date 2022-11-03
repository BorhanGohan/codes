x=2
str1=''
while x<=4:
    if x<4:
        str1=str1+str(x)+','
    else:
        str1=str1+str(int(x))
    x=x+0.25
print(str1)