import random

NUM_OF_CARDS = 3
cards = [('r', 'r'), ('b', 'b'), ('r', 'b')]

def chooseCardAndSide():
    # Choose card at random from all cards
    chosenCard = random.randint(0,NUM_OF_CARDS-1)
    chosenSide = random.randint(0,1)
    return (chosenCard, chosenSide)

def chooseOtherSide(notCard, notSide):
    # Keep choosing cards, until one is chosen that is not notCard
    while True:
        cardChoice = random.randint(0, NUM_OF_CARDS-1)
        sideChoice = random.randint(0, 1)
        if cardChoice != notCard and sideChoice != notSide:
            break

    return  (cardChoice, sideChoice)

def main():
    myCardNo, mySideNo = chooseCardAndSide()

    actualCard = cards[myCardNo]
    actualSide = actualCard[mySideNo]

    print('You chose card: ', actualCard)
    print(' You chose side: ' + actualSide)

    redCount = 0
    blueCount = 0
    for x in range(10000):
        otherCard, otherSide = chooseOtherSide(myCardNo, mySideNo)
        thisCard = cards[otherCard]
        if thisCard[otherSide] == 'r':
            redCount += 1
        else:
            blueCount += 1

    print('reds = ', redCount)
    print('blues = ', blueCount)


if __name__ == "__main__":
    main()
