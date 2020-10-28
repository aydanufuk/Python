class Card:
    def __init__(self, rank, suit):
        self.__rank = str(rank)
        self.__suit = suit

    def getRank(self):
        return self.__rank

    def getSuit(self):
        return self.__suit

    def getValue(self):
        if self.__rank == "Ace":
            return 1
        elif self.__rank == "Jack":
            return 11
        elif self.__rank == "Queen":
            return 12
        elif self.__rank == "King":
            return 13
        else:
            return eval(self.__rank)

    def isFaceCard(self):
        if self.__rank == "Jack" or self.__rank=="Queen" or self.__rank=="Ace":
            return True
        else:
            return False

    def __str__(self):
        cardString = ""
        cardString = str(self.__rank) + str(self.__suit)
        return cardString

