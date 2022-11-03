import random

random.seed(2)

FaceFreq = [0, 0, 0, 0, 0, 0]

for n in range(600000):
#    RollFace = random.randrange(1,7)
    RollFace = int(random.uniform(1,7))
#    RollFace = int(random.random()*6 + 1)
    FaceFreq[RollFace-1] += 1

for i in range(6):
#    print('Face '+str(i+1)+' showed '+ str(FaceFreq[i])+' times.')
     print(FaceFreq[i])
