InFile = open('e:\csc101\AI-NYTimes.txt', 'r')

Text = []

for Line in InFile:
    Text.append(Line)

InFile.close()

SentInDoc = []
WordsInDoc = []
NumOfWords = []
CharInWords = []

for i in range(len(Text)):
    SentInPara = Text[i].split('. ')

    for j in range(len(SentInPara)):
        SentInDoc.append(SentInPara[j])

        Words = SentInPara[j].split(' ')
        NumOfWords.append(len(Words))
        WordsInDoc += Words

FreqSenLen = []
for i in range(12):
    FreqSenLen.append(0)

for i in range(len(NumOfWords)):
    ii = int(NumOfWords[i]/5) + 1
    FreqSenLen[ii] += 1

for i in range(12):
    print(FreqSenLen[i])
    
input()

for Ch in WordsInDoc:
    CharInWords.append(len(Ch))

FreqWordLen = []
for i in range(19):
    FreqWordLen.append(0)

for i in range(len(CharInWords)):
    ii = CharInWords[i]
    FreqWordLen[ii] += 1

for i in range(19):
    print(FreqWordLen[i])
input()

UniqueWords = []
for x in WordsInDoc:
    for y in UniqueWords:
        if x == y:
            break
    else:
        UniqueWords.append(x)

FreqUniq = []

for i in range(0, 557):
    FreqUniq.append(0)

i = 0    
for y in UniqueWords:
    for x in WordsInDoc:
        if y == x:
            FreqUniq[i] += 1
    i += 1

#FreqUniq.sort()
#FreqUniq.reverse()

for i in range(0,len(FreqUniq)):
    MaxFreq = FreqUniq[i]
    for j in range(i+1,len(FreqUniq)):
        if FreqUniq[j] > MaxFreq:
            MaxFreq = FreqUniq[j]
            MaxLoc = j
    Buffer = FreqUniq[MaxLoc]
    FreqUniq[MaxLoc] = FreqUniq[i]
    FreqUniq[i] = Buffer
    Buffer = UniqueWords[MaxLoc]
    UniqueWords[MaxLoc] = UniqueWords[i]
    UniqueWords[i] = Buffer
    
    
for i in range(40):
    print(UniqueWords[i],FreqUniq[i])
