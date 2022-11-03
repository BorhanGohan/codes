# import random
# # for i in range(0,25):
# #     i=random.randint(25,100)
# #     print(i ,end=' ')
# mylist=[]
# for i in range(0,100):
#     num=random.randint(25,75)
#     mylist.append(num)
# print(mylist)
# largest=mylist[0]
# smallest=mylist[0]
# for i in mylist:
#     if i>largest:
#         largest=i
#     if i<smallest:
#         smallest=i
#         average=num/len(mylist)
# print('average:',average)
# print('largest:',largest)
# print('smallest:',smallest)



# import random
# mylist=[]
# for i in range(0,100):
#     num=random.randint(25,75)
#     mylist.append(num)
#     print(num,end=' ')
# print()
# print(mylist)
# largest=mylist[0]
# smallest=mylist[0]
# for i in mylist:
#     if i>largest:
#         largest=i
#     if i<smallest:
#        smallest=i
# average=num/len(mylist)
# print('average',average)
# print('largest:',largest)
# print('smallest:',smallest)










# import random
# mylist=[0]
# n=int(input('Enter the size of list:'))
# for i in range(0,n,1):
#     num=random.randint(20,40)
#     mylist.append(num)
#     print(num,end=',')
# print()
# x=int(input('Enter a number to search in list:'))
# found=False
# for i in mylist:
#     if x==i:
#         found=True
# if found==True:
#     print('Value is found')
# else:
#     print('Value not found')

# import random
# mylist=[]
# n=int(input('Enter the number of integers:'))
# for i in range(0,n,1):
#     i=random.randint(0,n)
#     mylist.append(i)
# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)

# import random
# mylist=[]
# a=int(input())
# b=int(input())
# for i in range(0,25):
#     n=random.randint(a,b)
#     mylist.append(n)
# print(mylist)

# import random
# mylist=[0]
# a=int(input('Enter the length of the list:'))
# 
# for i in range(0,a):
#     n=random.randint(0,25)
#     mylist.append(n)
# print(mylist)
# print()
# x=int(input('Enter a number to search in list:'))
# found=False
# for i in mylist:
#     if x==i:
#         found=True
# if found==True:
#     print(x,end='')




# import random
# mylist=[]
# for i in range(0,10):
#     i=random.randint(22,50)
#     mylist.append(i)
# print(mylist)

# import random
# number=random.randint(1,6)
# print(number)
# mylist=[]
# for i in range(10):
#     number=random.randint(22,50)
#     mylist.append(number)
# print(mylist)

# import random
# mylist=[]
# for i in range(0,10):
#     i=random.randint(22,50)
#     mylist.append(i)
# for i in mylist:
#     print(i ,end=",")





# name=input('Enter your name:')
# phone_no=input('Enter your phone number:')
# shipping_address=input('Enter your shipping address:')
# email_address=input('Enter your email address:')

# copies=int(input('How many copies would you like to order?:'))
# total_cost= copies * 300
# 
# if copies>20:
#     shipping_charge=500
#     cost_altogether=total_cost+shipping_charge
#     print('\n\t\t*YOUR BILL*')
#     print('\nYour shipping charge:',500)
#     print('Your total bill without shipping charge:',total_cost)
#     print('Your total bill with shipping charge:',cost_altogether)
# elif copies>=1 and copies<=20:
#     shipping_charge=(35/100)*total_cost
#     cost_altogether=total_cost+shipping_charge
#     print('\n\t\t*YOUR BILL*')
#     print('\nYour shipping charge:',shipping_charge)
#     print('Your total bill without shipping charge:',total_cost)
#     print('Your total bill with shipping charge:',cost_altogether)
# else:
#     print('Invalid input!')


# import random
# mylist=[]
# for i in range(0,100):
#     num=random.randint(0,100)
#     mylist.append(num)
# 
# print(mylist)
# largest=mylist[0]
# smallest=mylist[0]
# for i in mylist:
#     if i>largest:
#         largest=i
#     if i<smallest:
#         smallest=i
#         average=num/len(mylist)
# print('average:',average)
# print('largest:',largest)
# print('smallest:',smallest)


# import random
# mylist1=[float()]
# mylist2=[float()]
# for i in range(20):
#     a=random.randomfloat(1,20)
#     mylist1.append(a)
# print('*UNSORTED*')
# 
# for i in mylist1:
#     print(i,end=',')
# print('\n*SORTED*')
# mylist1.sort()
# for i in mylist1:
#     print(i,end=',')
# print('\n*DESCENDING ORDER*')
# mylist1.sort(reverse=True)
# for i in mylist1:
#     print(i,end=',')
# print()
# for i in range(20):
#     b=random.randint(1,20)
#     mylist2.append(b)
# print('\n*UNSORTED*')
# for i in mylist1:
#     print(i,end=',')
# print('\n*SORTED*')
# mylist2.sort()
# for i in mylist1:
#     print(i,end=',')
# print('\n*ASCENDING ORDER*')
# for i in mylist1:
#     print(i,end=',')

# import random
# mylist=[]
# for i in range(0,10):
#     i=random.randint(22,50)
#     mylist.append(i)
# for i in mylist:
#     Print(i ,end=",")


# print('\033[1m' + 'WELCOME TO FAHIMBOOKSTORE' + '\033[0m')
# 
# def hello():
#     name=str(input("enter your name : "))
#     print("hello " + str(name)+" Please enter your email address")
#     return
# hello()
# email_address = input("What is your email address? ")
# while "@" not in email_address:
#     email_address = input("Your email address must have '@' in it\nPlease write your email address again: ")
#     if len(email_address) <= 6 :
#         email_address = input("Your email address is too short\nPlease write your email address again: ")
#     if "." not in email_address:
#         email_address = input("Your email address must have '.' in it\nPlease write your email address again: ")
# while "." not in email_address:
#     email_address = input("Your email address must have '.' in it\nPlease write your email address again: ")
#     if len(email_address) <= 6 :
#         email_address = input("Your email address is too short\nPlease write your email address again: ")
#     if "@" not in email_address:
#         email_address = input("Your email address must have '@' in it\nPlease write your email address again: ")
# def address():
#     add=str(input("Enter the Adress : "))
#     number=str(input("Enter Phone number : "))
#     
#     print("Your Adress is :" + str(add))
#     print("Your Phone number is :" + str(number))
#     
#     return
# address()
# countbooks=int(input("How many copies do you want ?"))
# total = countbooks * 300
# if countbooks >=1 or countbooks <=3:
#   print ("your total bill is ",total)
#   from tqdm import tqdm
#   loop =tqdm (total =3000,position=0 , leave=False)
#   for k in range (3000):
#     loop.set_description("Processing your order".format(k))
#     loop.update(1)
#   loop.close()
#   print ("Your Order has been placed")
# else :
#   print ("Please input less number")



# import os
# location='poem.txt'
# flag=os.path.isfile(location)
# if flag:
#     size=os.path.getsize(location)
#     print(f'The {location} is {size} bytes')

# quote=open('quote.txt','r')
# count=dict()
# for line in quote:
#   line=line.lower()
#   words=line.split()
#   for word in words:
#     if word in count:
#       count[word]+=1
#     else:
#       count[word]=1
# print(count)


# import random
# mylist=[]
# n=int(input('Enter the size of list:'))
# for i in range(0,n,1):
#     num=random.randint(20,40)
#     mylist.append(num)
# for i in mylist:
#     print(i,end=',')
# print()
# x=int(input('Enter a number to search in list:'))
# indices=[]
# found=False
# for i in mylist:
#     if x==i:
#         found=True
# if found==True:
#     print('Value is found')
# else:
#     print('Value not found')
# for i in range(len(mylist)):
#     if x==mylist[i]:
#         indices.append(i)
# for i in indices:
#     print(i,end=',')
# print()
# # print(indices)
# count=0
# for i in range(len(mylist)):
#     if i==x:
#         count+=1
# print(count)

# print(indices)
# found=False
# indices=[]
# for i in range(len(mylist)):
#     if x==i:
#         indices.append(x)
# for i in indices:
#     print(i,end=',')
#         print(indices.index())
#     else:
#         print('Value not found')
#         found=True
#     if found==True:

# import random
# mylist=[]
# n=int(input('Enter the size of list:'))
# for i in range(0,n,1):
#     num=random.randint(20,40)
#     mylist.append(num)
# for i in mylist:
#     print(i,end=',')
# print()
# x=int(input('Enter a number to search in list:'))
# indices=[]
# found=False
# for i in mylist:
#     if x==i:
#         found=True
# if found==True:
#     print('Value is found')
# else:
#     print('Value not found')
# for i in range(len(mylist)):
#     counter=mylist.count(x)
#     if x==mylist[i]:
#         indices.append(i)
# for i in indices:
#     print(i,end=',')
# print()
# print(counter)
# print()
# counter=mylist.count(x)
# for i in range(len(indices)):
    #if x==mylist[i]:
        #count=count+1 





# def function1(x):
#     return x**2
# x=20
# print(function1(x))
# name=input('Enter your name:')
# shipping_address=input('Enter your shipping address:')
# mylist=['1.Anna Karenina by Leo Tolstoy','2.Madame Bovary by Gustav Flaubert','3.War and Peace by Leo Tolstoy','4.Lolita by Vladimir Nabokov','5.The Adventures of Huckleberry Finn by Mark Twain','6.Hamlet by William Shakespeare','7.The Great Gatsby by F. Scott Fizgerald','8.In Search of Lost Time by Marcel Proust','9.The Stories of Anton Chekhov by Anton Checkhov','10.Middlemarch by George Eliot']
# for i in mylist:
#     print(i)
# print()
# select=(int(input('Select the book from the list:')))
# for i in range(0,11):        
#     if select==i:
#         print(mylist[i-1])
# copies=int(input('\nHow many copies would you like to order?:'))
# total_cost= copies * 300
# if copies>=1 and copies<=3:
#     print('\n\t*YOUR BILL*')
#     print('Your total bill is',total_cost)
#     print('Ordered by:',name)
#     print('Estimated time of delivery: 3 Days.')
#     print('Shipping address:',shipping_address)
# elif copies>3:
#     print('Please input less number')
# else:
#     print('Invalid input!')    
    
# name=input('Enter your name:')
# shipping_address=input('Enter your shipping address:')
# mylist=['1.Anna Karenina by Leo Tolstoy','2.Madame Bovary by Gustav Flaubert','3.War and Peace by Leo Tolstoy','4.Lolita by Vladimir Nabokov','5.The Adventures of Huckleberry Finn by Mark Twain','6.Hamlet by William Shakespeare','7.The Great Gatsby by F. Scott Fizgerald','8.In Search of Lost Time by Marcel Proust','9.The Stories of Anton Chekhov by Anton Checkhov','10.Middlemarch by George Eliot']
# for i in mylist:
#     print(i)
# print()
# select=(int(input('Select the book from the list:')))
# for i in range(0,11):        
#     if select==i:
#         print(mylist[i-1])
# copies=int(input('\nHow many copies would you like to order?:'))
# total_cost= copies * 300
# if copies>=1 or copies<=3:
#   from tqdm import tqdm
#   loop=tqdm (total=1000,position=0,leave=False)
#   for k in range (1000):
#     loop.set_description("Processing your order".format(k))
#     loop.update(1)
#   loop.close()
#   print()
#   print("Your Order has been placed")
#   print('\n\t*YOUR BILL*')
#   print('Your total bill is',total_cost)
#   print('Ordered by:',name)
#   print('Estimated time of delivery: 3 Days.')
#   print('Shipping address:',shipping_address)
# elif copies>3:
#   print('Please input less number')
# else:
#   print('Invalid input!')   


# def books(name):
#     for i in
#     print('1.',name)
# books('Anna Karenina by Leo Tolstoy')


#def bill1():
#    f= open("TOTAL BILL FOR ALOM.txt","w+")
 #   f.write("NAME OF THE BOOK :\r\n" )
  #  f.write("BOOKS ORDERD :\r\n")
   # f.write("QUANTITY :\r\n")
#f.write("TOTAL PRICE :\r\n")
#    f.write("TOTAL PRICE WITH SHIPPING CHARGE :\r\n")
#    f = open("TOTAL BILL For ALOM.txt", "r")
#    print(f.read())
#bill1()
#    
#def bill2():
#    f= open("TOTAL BILL For SHAHIN.txt","w+")
#    f.write("NAME OF THE BOOK :\r\n" )
#    f.write("BOOKS ORDERD :\r\n")
#    f.write("QUANTITY :\r\n")
#    f.write("TOTAL PRICE :\r\n")
#    f.write("TOTAL PRICE WITH SHIPPING CHARGE :\r\n")
#    f = open("TOTAL BILL For SHAHIN.txt", "r")
#    print(f.read())
#bill2()

#ans =(input("For Customer 1 bill copy press 1 \r\nFor customer 2 bill copy press 2" ))
#if ans == "1":
#    bill1()
#elif ans == "2":
#    bill2#\

# num=[2,-3,5,99,6,32]
# import random
# num=[]
# for i in range(0,10):
#     n=random.randint(0,10)
#     num.append(n)
# for i in num:
#     print(i,end=',')
# print()
# for i in range (0,len(num)):
#     for j in range(0,len(num)-i-1):
#         if num[j]>num[j+1]:
#             temp=num[j]
#             num[j]=num[j+1]
#             num[j+1]=temp
# print(num)

# def function(x):
#     print(x)
#     print('still in this function')
#     return 3*x
# a=function(6)
# print(a)


# name1='abc'
# height_m1=1
# weight_kg1=60
# 
# name2='efg'
# height_m2=1.5
# weight_kg2=90
# 
# name3='hij'
# height_m3=2
# weight_kg3=80
# 
# 
# def bmi_calculator(name,height_m,weight_kg):
#     bmi=weight_kg/(height_m**2)
#     print('bmi:')
#     print(bmi)
#     if bmi<25:
#         return name + 'not overweight'
#     else:
#         return name + 'is overweight'
# result1=bmi_calculator(name1,height_m1,weight_kg1)
# result2=bmi_calculator(name2,height_m2,weight_kg2)
# result3=bmi_calculator(name3,height_m3,weight_kg3)
# 
# 
# print(result1)
# print(result2)
# print(result3)



# def radius_sphere(r):
#     return (4/3)*3.1416*(r**3)
# volume=radius_sphere(float(input('enter:')))
# print(volume)

# def factorial(x):
#     factorial=1
#     if x<0:
#         print('negative')
#     elif x==0:
#         print('factorial of 0 is 1')
#     else:
#         for i in range(x+1):
#             factorial==factorial*i
# a=factorial(0)
# print(a)
# x=7
# factorial=1
# if x<0:
#     print('negative')
# elif x==0:
#     print('factorial of 0 is 1')
# else:
#     for i in range(1,x+1,1):
#         factorial==factorial*i
# print(factorial)
# 
# values = input("Input some comma seprated numbers : ")
# # list = values.split(",")
# list=[values]
# tuple = tuple(list)
# for i in list:
#     print(i,end=',')
#     print(tuple)



# mylist=[]
# n=int(input('Enter:'))
# for i in range(0,n+1):
#     mylist.append(i)
# fibonacci=[]
# f=0
# s=1
# fibonacci.append(f)
# fibonacci.append(s)
# for i in range(1,n):
#     final=f+s
#     f=s
#     s=final
#     if final<=n:
#         fibonacci.append(final)
#         print(final,end=',')

# import random
# A = []
# for i in range(10):
#     n = random.randint(1,100)
#     A.append(n)
# for i in range(len(A)):
#     for j in range(0, len(A) - i - 1):
#         if A[j] > A[j + 1]:
#             temp = A[j]
#             A[j] = A[j+1]
#             A[j+1] = temp
# A.sort()
# print(A)
# first_max=A[len(A)-1]
# second_max=A[len(A)-2]
# print('1st max:',first_max)
# print('2nd max:',second_max)
# print(f"1st minimum = {A[0]}")
# print(f"2nd minimum = {A[1]}")
# print(f"Median = {A[5]}")
# average=(len(A)+1)//2
# median=A[average]
# print(median)

# print(f"1st maximum = {A[10]}")
# print(f"2nd maximum = {A[9]}")



# mylist = [1,2,3,4,5]   
# a= 0
# for i in range(1,len(mylist)):
#     if (mylist[i] < mylist[i-1]):
#         a = 1
#     i =i + 1
# if a==0:
#     print ("Yes, List is sorted.")
# else :
#     print ("No, List is not sorted.")

# mylist = [19,21,24,51,67]
# print(mylist)
# for i in range(len(mylist)-1):    
#     if mylist[i] <= mylist[i + 1]:  
#         print()
#     print("Yes, List is sorted.")
#     else:
#         print("No, List is not sorted.")



# mylist=[4,2,3,3,5,6]
# flag=0
# for i in range(1,len(mylist)):
#     if i<=i-1: #or i>=i+1:
#         flag=1
# if flag==0:
#     print('sorted.')
# else:
#     print('not sorted')

    
# num = [1,2,3,4,5]   
# a= 0
# for i in range(len(num)):
#     if i==len(num)-1:
#         break
#     if (num[i] > num[i+1]):
#         a = 1
#     i =i + 1
# if a==0:
#     print ("Yes, List is sorted.")
# else :
#     print ("No, List is not sorted.")
# import random
# num=[]
# for i in range(10):
#     n=random.randint(0,50)
#     num.append(n)
# num.sort(reverse=True)
# print()
# print(num)
# print()




# num = [1,2,3,4,5,5,6,66,67,71,71,77,78]   
# num=[]
# a=True
# b=True
# for i in range(5):
#     n=int(input('enter:'))
#     num.append(n)
# print(num)
# for i in range(len(num)-1):
#     if i==len(num)-1:
#         break
#     if num[i]<num[i+1]:
#         a=False
#     i=i+1
# for i in range(len(num)-1):
#     if i==len(num):
#         break
#     if num[i]>num[i+1]:
#         b = False
#     i=i+1
# if a==True:
#     print ("Yes, List is sorted. It is in descending form.")
# elif b==True:
#     print ("Yes, List is sorted. It is in ascending form.")
# else:
#     print('not sorted')



#for descending order
                        
# list1=[1,1,1,4,4,5,5,5,4]
# 
# print(list1)
# flag=True
# for i in range(len(list1)):
#     if i==len(list1)-1:
#         break
#     if list1[i]>list1[i+1]:
#         flag=False
#     i+=1
# if flag==True:
#     print("the list is  sorted")
# else:
#     print("the list not sorted")




# def word_count(s):
#     counter=0
#     for i in s:
#         if i==' ':
#             counter+=1
#     return counter+1
# s=input('enter:')
# 
# print(word_count(s))


# def triangle(n):
#     for i in range(1,n+1,1):
#         for j in range(1,n+1-i,1):
#             print(' ',end='')
#         for j in range(1,i+1,1):
#             print('B',end='')
#         for j in range(1,i,1):
#             print('O',end='')
#         print()
# n=int(input('Enter n:'))
# triangle(n)
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(' ',end='')
#     for j in range(1,n+1-i,1):
#         print('*',end='')
#     for j in range(1,n-i,1):
#         print('*',end='')
#     print



# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# n=int(input('enter:'))
# a=factorial(n)
# print(a)


# def digits(n):
#     count=0
#     for i in range(n):
#         if n!=0:
#             n=n//10
#             count+=1
#     return count
# n=int(input('ENTER:'))
# a=digits(n)
# print(a)


# def sum_digits(a):
#     sum=0
#     for i in range(a):
#         sum=sum+i
#         i+=1
#     return sum
# a=int(input('enter:'))
# print(sum_digits(a))



# def iub_id(ID):
#     if ID[0]=='I' and ID[1]=='U' and ID[3]=='B':
#         print('ID is Valid')
#     else:
#         print('ID is not Valid')
# 
# ID=[(input('enter:'))]
# iub_id(ID)

# mylist=[]
# n=int(input('enter:'))
# for i in range(n+1):
#     mylist.append(i)
# print(mylist)
# print()
# prime=[]
# check=True
# for num in range(1,len(mylist)+1):
#    if num >= 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num,end=',')


# for num in range(20):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#         else:
#             print(num)
#             break



# num=int(input())
# for i in range(3,num):
#     if num%i==0:
#         print('not prime')
#         break
#     else:
#         print('prime')
#         break


# Lower = 1
# Upper = 50
# for num in range(Lower, Upper + 1):
#    if num >= 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num,end=',')


# a=int(input("Enter first Number: "))
# b=int(input("Enter second Number: "))   
# for n in range(a,b+1):
#     temp=n 
#     rev=0 
#     for i in range(0,n):
#         rev=(rev*10)+(n%10)
#         temp=temp//10
#         if n==rev:
#             print(n,end=',')        




                               #ORIGINAL MANE TEMP


# def prime_checker(numbers):
#     counter = 0
#     for i in range(len(numbers)):
#         prime = True
#         print(i)
#         for j in range(2,numbers[i]): # i = 5 | 2,3,4  
#             if i%j==0:
#                 prime = False
#             if prime == True:
#                 counter=counter+1
#    
#     print("No of prime numbers = ", counter)
# 
# numbers = [2,4,10,7,5]
# prime_checker(numbers)

# def prime_checker(numbers):
#     counter = 0
#     prime = True
#     for i in range(0,len(numbers)):
#         if numbers[i]%(i+1)==0:
#             prime=False
#         else:
#             counter+=1
#     if prime==False:
#         print('counter:',counter)
#     else:
#         print('no prime numbers')
# 
# numbers = [2,4,10,7,5]
# prime_checker(numbers)




# def getName():
#     name=input('Name:')
#     return
# def getAge():
#     age=int(input('Age:'))
#     return
# def getMarkOfCSC101():
#     mark=int(input('Marks:'))
# # def printAllInfo(allInfo):
# #     for info in allInfo:
# #         print(info)
# def evaluateMark(studentmark,nstudentName):
#     if studentmark>90:
#         print(f'{name} got A')
#     else:
#         print('Not a good grade')
# 
# studentName=getName()
# studentAge=getAge()
# studentmark=getMarkOfCSC101()
# evaluateMark()
        
# x=int(input('Enter value of x:'))
# for i in range(10):
#     if x==i:
#         print('They are equal to',i)
#     else:
#         print('not to',i)
# values=input()
# 
# list=values.split(',')
# # list.split(',')
# print('\n')
# print(list)
#
# values=input('Input some comma separated numbers:')
# list=values.split(',')
# tuple=tuple(list)
# print('List:',list)
# print('Tuple:',tuple)

#Write a Python program to accept a filename from the user and print the extension of that'''
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print(f_extns)
# print ("The extension of the file is : " + repr(f_extns[-1]))
# print(str(f_extns[-1]))

#Write a Python program to display the first and last colors from the following list'''
# color_list=['Red','Green','White','Black']
# first_color=color_list[0]
# last_color=color_list[-1]
# print('first color:',first_color,'\nlast color:',last_color)

#Write a Python program to display the examination schedule. (extract the date from exam_st_date).'''
# exam_st_date=(11,12,2014)
# date=int(input('date:'))
# month=int(input('month:'))
# year=int(input('year:'))
# exam_st_date=(date,month,year)
# print('The examination will start from: %i/%i/%i'%exam_st_date)

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.'''
# n=int(input('Enter n:'))
# n1=int('%i'%n)
# n2=int('%i%i'%(n,n))
# n3=int('%i%i%i'%(n,n,n))
# print('result:',n1+n2+n3)
#
# abs=11.211
# 
# print(abs.__doc__)

#Write a Python program to print the calendar of a given month and year.'''

# import calendar
# y=int(input('enter year:'))
# m=int(input('enter month:'))
# print(calendar.month(y,m))

#Write a Python program to print the following 'here document'.'''

# print('''
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# ''')

# import datetime
# y=int(input('enter year:'))
# m=int(input('enter month:'))
# d=int(input('enter date:'))
# print(datetime.date(y,m,d))



#find totals days'''

# from datetime import date
# f_date=date(2014,7,2)
# l_date=date(2014,8,11)
# total_days=l_date-f_date
# print(total_days.days)


# a=int(input('enter a number:'))
# if a>17:
#     b=(a-17)*2
#     print('result is',b)
# else:
#     b=17-a
#     print('result is',b)

# def result(n):
#     if n>17:
#         return(n-17)*2
#     else:
#         return 17-n
# result(int(input('enter a number:')))
# print('result is',result())

# name='Borhan'
# message=f'Hi, my name is {name}'
# print(message.upper())
# print(message.lower())
# print(message.title())
# print(message.find('m'))
# print(message.replace('m','q'))
# print(message[0])

# course='python can be python also can be \
#     python'
# contains='python' in course
# print(contains)


#Write a Python program to test whether a number is within 100 of 1000 or 2000.'''
# n=int(input('enter:'))
# def within_100(n):
#     if abs(1000-n)<=100 or abs(2000-n)<=100:
#         return True
#     else:
#         return False
# print(within_100(n))

#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.'''
# def sum(a,b,c):
#     if a==b==c:
#         return 3*(a+b+c)
#     else:
#         return a+b+c
# a=int(input('a'))
# b=int(input('b'))
# c=int(input('c'))
# print(f'the result is {sum(a,b,c)}')

# Write a Python program to get a new string from a given string where "Is" has been added to the front.
#If the given string already begins with "Is" then return the string unchanged.
# user=input('enter sentence, start with capital letter:')
# def sentence(user):
#     if user[:2]=='Is':
#         return user
#     else:
#         return 'Is'+' '+user
# print(sentence(user))

#Write a Python program to get a string which is n (non-negative integer) copies of a given string.'''
# def line(user,n):
#     new_line=''
#     for i in range(n):
#         new_line+=user
#     return new_line
# user=input('enter:')
# n=abs(int(input('num:')))
# print(line(user,n))

#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.'''
# def evenodd(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
# n=int(input('enter:'))
# print(evenodd(n))

#Write a Python program to count the number 4 in a given list.'''
# import random
# def mylist(nums):    
#     for i in range(10):
#         n=random.randint(1,10)
#         nums.append(n)
#     print(nums)    
#     counter=0
#     for i in nums:
#         if i==4:
#             counter+=1
#     return counter
# print(mylist([]))
# '''Count vowels in python using function'''
# def vowels(v_letters,user):
#     for i in v_letters:
#         if i==user:
#             return 'Vowel'
#     if i!=user:
#         return 'not vowel'
# user=input('Enter a letter:')
# print(vowels(['a','e','i','o','u'],user))
        
# user=input('Enter a letter:')
# vowels=['a','e','i','o','u']
# flag=False
# for i in vowels:
#     if user==i:
#         flag=True
# if flag==True:
#     print('vowel')
# else:
#     print('not vowel')

# def vowel_identify(user, vowel):
#     for i in vowel:
#         if user==i:
#             return 'vowel'
#     return 'not vowel'    
# user=input('Enter a letter:')
# print(vowel_identify(user, ['a','e','i','o','u']))

# def num(mylist,user):
#     for i in mylist:
#         if i==user:
#             return True
#     return False    
# user=int(input('Enter a number to check:'))
# print(num([1,5,8,3,10],user))









