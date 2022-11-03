import random
A = []
for i in range(10):
    n = random.randint(1,100)
    A.append(n)
for i in range(len(A)):
    for j in range(0, len(A) - i - 1):
        if A[j] > A[j + 1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
# A.sort()
print(A)
first_max=A[len(A)-1]
second_max=A[len(A)-2]
print('1st max:',first_max)
print('2nd max:',second_max)
print(f"1st minimum = {A[0]}")
print(f"2nd minimum = {A[1]}")
print(f"Median = {A[5]}")
average=(len(A)+1)//2
median=A[average]
print(median)