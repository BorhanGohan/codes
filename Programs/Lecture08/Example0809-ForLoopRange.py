# Demonstration of range funtion in for-loop.

# This cose chooses values of num fron 0 to 14, and prints the square and
# cube of the number.

for num in range(10):
    print(format(num,'4d'), format(num*num,'6d'), format(num**3,'6d'))

input()

# We can specify selection in the range function. In this cose the values
# of num is chosesn staarting from 5, till 14, and prints the aquare-root
# and cube root of the number.

for num in range(5, 15):
    print(format(num,'5.1f'), format(num**0.5,'10.6f'), format(num**(1/3),'10.6f'),) 

input()

# In addition to specifying the selestion, we can specify the step also

Sum = 0.0
for num in range(0, 20, 2):
    Sum += num
print('Sum of integers 0 to 19, in an interval of 2 is: '+str(Sum))

input()

# Using the step, if required, we can choose the numbers in reverse
# order within the range.

Product = 1
for num in range(20,2,-2):
    print(num, end=' ')
    Product *= num
print()
print('Multilication result: '+str(Product))
