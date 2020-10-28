from Hand import Hand


class BlackJackHand(Hand):
    def __inti__(self):
        super().__init__()

    def getValue(self):
        value = 0

        for i in range(0, self.getNumCards()):
            card = self.getCard(i)
            if card.isFaceCard():
                value += 10
            elif card.getRank() == "Ace":
                value += 11
            else:
                value += card.getValue()

        return value


    #def __str__(self):
    #    if self.getNumCards() == 0:
     #       return "empty hand"
      #  else:
       #     standardString = super().__str__()
        #    return  "XX" + standardString[2:]