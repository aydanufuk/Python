from Card import Card
from Hand import Hand
from BlackJackHand import BlackJackHand


def main():
    myHand = BlackJackHand()
    myHand.addCard(Card(3, "Hearts"))
    myHand.addCard(Card("Queen", "Clubs"))
    myHand.addCard(Card("Ace", "Spades"))

    print(myHand)
    print("hand total value: ", myHand.getValue())


main()
