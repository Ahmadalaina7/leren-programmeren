import random
"""
Generate the UNO deck of 108 cards.
parametrs : None
Return values: Deck->List
"""
def buildDeck():
    deck = []
    colours = ["Red" , "Green" , "Yellow" , "Blue"]
    values = [0,1,2,3,4,5,6,7,8,9," Draw Two" , "Skip" , "Reverse"] 
    wilds = ["Wild" , "Wild Draw Four"]
    for colour in colours:
        for value in values:
            cardVal = "{} {}".format(colour, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range (4):
        deck.append(wilds[0])
        deck.append(wilds[1] )   
    return deck
"""
Shuffle a list of items passed into it
Parameters: deck->list
return values: deck->list
"""
def shuffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0,107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck
"""
Draw cad function that draws a specified number off the top of the deck
parameters: numCards->int
returns: cardsDrwan -> list
""" 
def drwanCards(numCards):
    cardsDrawn=[]
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn
"""
print formatted list of player's hand
parameter: player->int, playerHand->list
Return: None
"""
def showHand(player , playerHand):
    print("player {}'s Turn".format(player+1))
    print("Your Hand")
    print("-----------------")
    y = 1
    for card in playerHand:
        print("{}) {}".format(y,card))
        y+=1
        print("")
"""
check whether a player is able to play a card, or not
paramteres: colour->String, value->list , playerHand->list
Return: boolean
"""

def canPlay(colour, value, playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False

unoDeck =  buildDeck()
unoDeck = shuffleDeck(unoDeck)
discards = []
print(unoDeck)
players = []
numplayers = int(input("How many players? "))
while numplayers<2 or numplayers>4:
    numplayers = int(input("Invalid. pleas enter a number between 2-4.How many players? "))
for player in range(numplayers):
    players.append(drwanCards(5))
print(players)
playerTurn = 0
playDirection = 1 
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColour = splitCard[0]
if currentColour != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

while playing:
    showHand(playerTurn,players[playerTurn])
    print("Card on top of discard pile: {} ".format(discards[-1]))
    if canPlay(currentColour, cardVal,players[playerTurn]):
        cardChosen = int(input("Wich card do you want to play? "))
        while not canPlay(currentColour , cardVal,[players[playerTurn][cardChosen-1]]):
            cardChosen = int(input("Not a valid card. Wich card do you want to play? "))
        print("You played {}".format(players[playerTurn].pop(cardChosen-1)))
        discards.append(players[playerTurn][cardChosen-1])
    else:
        print("You can't play. You have to drwa a card")
        players[playerTurn].extend(drwanCards(1))
    print("")
    playerTurn += playDirection
    if playerTurn == numplayers:
        playerTurn = 0

    elif playerTurn < 0:
        playerTurn = numplayers-1