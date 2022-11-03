import random

random.seed(2)

SumFreq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for n in range(360000):
    FirstRollFace = int(random.uniform(1,7))
    SecondRollFace = int(random.uniform(1,7))
    TwoRollsSum = FirstRollFace + SecondRollFace
    SumFreq[TwoRollsSum-2] += 1

for i in range(11):
    print('Sum '+str(i+2)+' showed '+ str(SumFreq[i])+' times.')
