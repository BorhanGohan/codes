#########################
## EXAMPLE: functions as arguments
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20func_a(%29%3A%0A%20%20%20%20print('inside%20func_a'%29%0A%0Adef%20func_b(y%29%3A%0A%20%20%20%20print('inside%20func_b'%29%0A%20%20%20%20return%20y%0A%0Adef%20func_c(z%29%3A%0A%20%20%20%20print('inside%20func_c'%29%0A%20%20%20%20return%20z(%29%0A%0Aprint(func_a(%29%29%0Aprint(5%2Bfunc_b(2%29%29%0Aprint(func_c(func_a%29%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#########################
def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5+func_b(2))
print(func_c(func_a))
