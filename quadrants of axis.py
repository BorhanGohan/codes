x=int(input())
y=int(input())

if x>0 and y>0:
    print('1st quadrant')
elif x<0 and y>0:
    print('2nd quadrant')
elif x<0 and y<0:
    print('3rd quadrant')
elif x>0 and y<0:
    print('4th quadrant')
elif x==0 and y!=0:
    print('Y-axis')
elif x!=0 and y==0:
    print('X-axis')
elif x==0 and y==0:
    print('Origin')
else:
    print('Input correctly!')