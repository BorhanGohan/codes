InFile = open('e:\csc101\AI-NYTimes.txt', 'r')

Text = []

# Read the file.

for Line in InFile:
    Text.append(Line)

# Close the file.

InFile.close()

# Convert the paragraphs to sentences and sentences to words
# using string split() method.

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

# Find the frequency ot length of sentences in words.

FreqSenLen = []
for i in range(12):
    FreqSenLen.append(0)

for i in range(len(NumOfWords)):
    ii = int(NumOfWords[i]/5) + 1
    FreqSenLen[ii] += 1

for i in range(12):
    print(FreqSenLen[i])
    
input()

# Find the frequency of length of words.

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

