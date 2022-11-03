def word_count(s):
    counter=0
    for i in s:
        if i==' ':
            counter+=1
    return counter+1
s=input('enter:')

print(word_count(s))