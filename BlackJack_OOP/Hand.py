class Hand:
    def __init__(self):
        self.__cards = []
        self.__numCards = 0

    def addCard(self, card):
        self.__cards.append(card)
        self.__numCards += 1

    def getCard(self, index):
        if index < 0 or index >= self.__numCards:
            print("invalid index")
            return None
        else:
            return self.__cards[index]

    def removeCard(self, index):
        if index < 0 or index >= self.__numCards:
            print("invalid index")
            return None
        else:
            removed = self.__cards.pop(index)
            self.__numCards -= 1
            return removed

    def getNumCards(self):
        return self.__numCards

    # returns the total value of the cards in th hand
    def getValue(self):
        value = 0

        for card in self.__cards:
            value += card.getValue()

        return value

    # returns a string representation of the head

    def __str__(self):
        if self.__numCards == 0:
            return "empty hand"

        handString = ""

        for card in self.__cards:
            handString += str(card)
            #handString += str("|" + card.getRank() + " " + card.getSuit()) + "| "

        return handString
