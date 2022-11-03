
start_num=int(input('Enter a starting number:'))
end_num=int(input('Enter a ending number:'))
while start_num<=end_num:
    if start_num%2!=0:
        print(start_num,end=',')
    else:
        print(start_num,end='')
    start_num+=1