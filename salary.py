b_salary=int(input('Enter Basic Salary:'))

if b_salary<=10000:
    HRA=(20/100)*b_salary
    DA=(80/100)*b_salary
    salary=((b_salary)+(HRA))+((b_salary)+(DA))
    print(f'Actual Salary is {salary}')
elif b_salary<=20000:
    HRA=(25/100)*b_salary
    DA=(90/100)*b_salary
    salary=((b_salary)+(HRA))+((b_salary)+(DA))
    print(f'Actual Salary is {salary}')
elif b_salary>1000:
    HRA=(30/100)*b_salary
    DA=(95/100)*b_salary
    salary=((b_salary)+(HRA))+((b_salary)+(DA))
    print(f'Actual Salary is {salary}')
else:
    print("Input correctly!")