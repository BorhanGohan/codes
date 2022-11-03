def SomeFcn(a):
    b = a + 1
    c = b*b
    return (b,c)

x = 2.1
(y,z) = SomeFcn(x)
print(x, y, z)
