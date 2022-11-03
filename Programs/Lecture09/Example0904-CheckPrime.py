# Checks if an entered number is a Prime number

import math

num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,int(math.sqrt(num))+1):  
       if (num % i) == 0:  
           print(num,"is not a prime number")    
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")

if num==(4*num+1):
   print('number',num)

