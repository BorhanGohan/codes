def Circle(Radius):
    Pi = 3.14159
    Area = Pi*Radius*Radius
    Circumference = 2*Pi*Radius
    return (Area, Circumference)

Radius = float(input('Input radius of the circle: '))
(Area, Circumference) = Circle(Radius)
print('Area of circle              : '+str(Area))
print('Circumferrence of the circle: '+str(Circumference))
