# Find prime numbers beween a lower range and an upper range

Lower = 1
Upper = 50

print("Prime numbers between", Lower, "and", Upper, "are:")

for num in range(Lower, Upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
