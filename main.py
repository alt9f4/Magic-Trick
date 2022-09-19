import random

def disrupt(deck):
    print("\nWonderful, is there anything you'd like to see or do before the trick starts?")
    recursion = True
    while recursion == True:
        print("1. Look at the deck")
        print("2. Shuffle the deck")
        print("3. Nope")
        ans = input("Request: ")
        
        while ans != '1' and ans != '2' and ans != '3':
            ans = input("try again: ")
        if ans == '1':
            print("But of course, here you go\n")
            print(deck)
            print("\nIs there anything else I can help with?")
        if ans == '2':
            print("But of course, let us shuffle the cards")
            random.shuffle(deck)
            print("\nIs there anything else I can help with?")
        if ans == '3':
            recursion = False
    return deck


def cut(deck,x):
    #dividing both half
    print("Alright, lets go ahead and cut at the "+str(x)+"th position")
    d1=deck[0:x]
    d2=deck[x:52]
    deck = d2+d1
    return deck

deck = []
suite = [' of Spades',' of Hearts',' of Clubs',' of Diamonds']
rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

#creating a deck
for i in range(4):
    for j in range(13):
        num = 1+j
        card = rank[j]+suite[i]
        deck.append(card)

#shuffle
random.shuffle(deck)

#Start Game?
print("Come one come all")
ans = input("Would you like to see a magic trick?[y or n]\n")
while ans != 'y' and ans != 'n':
    ans = input("try again: ")
if ans == 'n':
    print("oh..")
if ans == 'y':
    #character selection
    print("\nCharacters")
    print("1. Entertained")
    print("2. Entertainer")
    character = input("Please select your character:\n")
    while character != '1' and character != '2':
        character = input("try again: ")

    if character == '1':

        #give the entertained a sense of control
        deck = disrupt(deck)

        #pick a card any card        
        print("\nAlright first things first, pick a card by inputing a number betweet 1 and 52:")
        ans = input()
        while ans.strip().isdigit() == False or int(ans) <= 1 or int(ans) >= 52:
            
            ans = input("try again: ")
        print("Alright lets pick your card at position", ans)

        card = deck[int(ans)-1]
        deck.remove(deck[int(ans)-1])

        print("you: I see so my card is:", card)

        #give the entertained a sense of control
        deck = disrupt(deck)

        print("\nAlright now lets put your card back on top and cut the cards, pick a number betweet 1 and 52 to know where to cut:")

        #use a key card to keep track of their cards without obviously looking at their cards
        bottom_card = deck[0]

        #placing card back on top of deck
        deck.append(card)

        ans = input()
        while ans.strip().isdigit() == False or int(ans) <= 1 or int(ans) >= 52:
            deck = cut(deck,ans)

        print("okay now let me try and guess your card here..")

        input("\npress enter for the big reveal")

        #use the key card to find their card
        guess =  deck.index(bottom_card)-1

        print("your card is:", deck[guess])

        
    if character == '2':
        print("\nhello there dear magician, today we will teach you a simple magic trick")
        input("press enter to continue")
        
        print("\nfirst lets have the person we are entertaining pick a card, remember it and put it on top of the deck face-down")
        rand_num =random.randint(0,51)

        #picked card remembered and put back on top
        card=deck[rand_num]
        deck.remove(deck[rand_num])
        deck.append(card)

        input("press enter to continue")

        print("\nperfect now lets remember the bottom card and let the person to cut the cards to give them a sense of participation and control")
        #bottom card remembered
        bottom_card = deck[0]

        #card cut
        rand_num =random.randint(0,51)
        deck = cut(deck,rand_num)

        
        input("press enter to continue")

        print("\nperfect, now ensure/agree with the person the person that their card is somewhere in the middle")

        input("press enter to continue")

        print("\nfinally, as we ensure the person, lets take a peek of the deck to find their card")
        print("now since we had cut the deck, the person's card should be right under the card we decided to remember")

        input("press enter to continue")
        
        guess =  deck.index(bottom_card)-1

        print("\nand their card should be the:",deck[guess])









            
        

