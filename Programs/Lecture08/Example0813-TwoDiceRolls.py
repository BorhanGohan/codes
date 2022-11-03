# Outcomes of two rolls of a fair dice

for i in range(6):
    for j in range(6):
        print('('+format(j+1,'1d')+','+format(i+1,'1d')+')',end=' ')
    print()
