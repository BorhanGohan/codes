a = float(input("Enter a number:"))
b = float(input("Enter a number:"))
c = float(input("Enter a number:"))
d = float(input("Enter a number:"))

if a>b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
else:
    print(d)
# if a>b:
#     if a>c:
#         if a>d:
#             print(f"{a} is the largest.")
#         else:
#             print(f"{d} is the largest.")
#     else:
#         if c>d:
#             print(f"{c} is the largest.")
#         else:
#             print(f"{d} is the largest.")
# else:
#     if b>c:
#         if b>d:
#             print(f"{b} is the largest.")
#         else:
#             print(f"{d} is the largest.")
#     else:
#         if c>d:
#             print(f"{c} is the largest.")
#         else:
#             print(f"{d} is the largest.")
# 