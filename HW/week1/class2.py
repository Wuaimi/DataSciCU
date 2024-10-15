class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def suitvalue(self):
        if self.suit == 'club':
            return 1
        elif self.suit == 'diamond':
            return 2
        elif self.suit == 'heart':
            return 3
        else:
            return 4

    def tenvalue(self):
        if self.value == '10':
            return 1
        elif self.value == 'J':
            return 2
        elif self.value == 'Q':
            return 3
        elif self.value == 'K':
            return 4

    def __str__(self):
        return f"({self.value} {self.suit})"

    def getScore(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == 'A':
            return 1
        else:
            return int(self.value)

    @staticmethod
    def sum(card1, card2):
        return (card1.getScore() + card2.getScore()) % 10

    def __lt__(self, rhs):
        ss = self.getScore()
        rs = rhs.getScore()

        if self.value == 'A':
            ss = 11
        elif ss == 2:
            ss = 12
        if rhs.value == 'A':
            rs = 11
        elif rs == 2:
            rs = 12

        if ss != rs:
            return ss < rs
        else:
            if self.value == rhs.value:
                return self.suitvalue() < rhs.suitvalue()

            if self.getScore() == 10:
                return self.tenvalue() < rhs.tenvalue()

        return False

# Example usage
n = int(input("Enter number of cards: "))
cards = []
for i in range(n):
    value, suit = input(f"Enter card {i+1} (value suit): ").split()
    cards.append(Card(value, suit))

for i in range(n):
    print(f"Score of {cards[i]}: {cards[i].getScore()}")
    
print("----------")
for i in range(n-1):
    print(f"Sum of {cards[i]} and {cards[i+1]}: {Card.sum(cards[i], cards[i+1])}")

print("----------")
cards.sort()
for card in cards:
    print(card)
