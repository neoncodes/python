# Second Time

class Card:
    def __init__(self, suit, card):
        self.suit = suit
        self.card = card

class Deck:
    def __init__(self):
        self.deck = self.createDeck()
    def createDeck(self):
        z = []
        for x in range(2,11):
            z.append(Card("Spades", str(x)))
        
        for x in range(2,11):
            z.append(Card("Diamonds", str(x)))
        
        for x in range(2,11):
            z.append(Card("Hearts", str(x)))
        
        for x in range(2,11):
            z.append(Card("Clubs", str(x)))
        
        k = ["Spades", "Clubs", "Diamonds", "Hearts"]

        for y in k:
            z.append(Card(y, "Jack"))
            z.append(Card(y, "Queen"))
            z.append(Card(y, "King"))
            z.append(Card(y, "Ace"))

        return z


    def print(self):
        for x in range(51):
            print(str(self.deck[x].card)+" of "+self.deck[x].suit,end="\n")
    #def shuffle(self):
    #    shuff

deck1 = Deck()
print(deck1.print())