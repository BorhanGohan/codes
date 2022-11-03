def PrintName(LastName, FirstName, Reverse):
    if Reverse:
        print(LastName+', '+FirstName)
    else:
        print(FirstName+' '+LastName)

PrintName('Karim', 'Abdul', False)
PrintName(FirstName='Abdul', LastName='Karim', True)
