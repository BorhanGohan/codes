filename = input("Input the Filename: ")
f_extns = filename.split(".")
print(f_extns)
print ("The extension of the file is : " + repr(f_extns[-1]))
print(str(f_extns[-1]))