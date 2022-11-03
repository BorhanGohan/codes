# num=int(input("Enter any number:"))
# rev=0
# while num!=0:
#     r=num%10
#     num=num//10
#     rev=r+rev*10
# print(rev)

number=int(input("Enter number :"))
rev_number=0
while(number >0):
  remainder=number % 10 
  rev_number=(rev_number*10)+remainder
  number=number//10
print(rev_number)