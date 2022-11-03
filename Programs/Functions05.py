x = 'awesome'
def myfunc():
    global x
    print('Python is ' + x) 
    x = 'fantastic'
    print('Python is ' + x)
myfunc()
print('Python is ' + x)
