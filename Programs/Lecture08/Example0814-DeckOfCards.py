# All the cards in a deck of a card

for i in ('2','3','4','5','6','7','8','9','Ace','King','Queen'):
    for j in('Diamonds', 'Spades', 'Clubs', 'Hearts') :
        CardName = '('+i+' of '+j+')'
        print(CardName+(19-len(CardName))*' ',end='')
    print()
