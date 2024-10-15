class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f"({self.value} {self.suit})"
    def getScore(self):
        value = 0
        if self.value == '2':
            value = 12
        elif self.value == 'A':
            value = 11
        elif self.value == 'K':
            value = 10
        elif self.value == 'Q':
            value = 9
        elif self.value == 'J':
            value = 8
        else:
            value = int(self.value) - 3
    
        value *= 4

        if self.suit == 'club':
            value += 1
        elif self.suit == 'diamond':
            value += 2
        elif self.suit == 'heart':
            value += 3
        else:
            value += 4  # for 'spade'
        return value

    @staticmethod
    def kvCard():
        deck = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
        suit = ['club', 'diamond', 'heart', 'spade']
        card_dict = {}
        for i in range(13):
            for j in range(4):
                C = Card(deck[i], suit[j])
                card_key = C.getScore()  
                card_value = (deck[i], suit[j])  
                card_dict[card_key] = card_value  

        return card_dict
    
    def next1(self):
        value = self.getScore()
        card_dict = Card.kvCard()
    
        if value != 52:
            next_card_value, next_card_suit = card_dict[value + 1]  # Access value and suit as a tuple
            return Card(next_card_value, next_card_suit)
        else:
            next_card_value, next_card_suit = card_dict[1]  # Wrap-around for the last card
            return Card(next_card_value, next_card_suit)

    def next2(self):
        c = self.next1()
        self.value = c.value
        self.suit = c.suit
        

    
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i]) 