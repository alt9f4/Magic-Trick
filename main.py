import random

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
    print("1. Entertainer")
    print("2. Entertained")
    character = input("Please select your character:\n")
    while character != '1' and character != '2':
        character = input("try again: ")

    if character == '1':
        pass
    if character == '2':
        print("\nAh wonderful, is there anything you'd like to see or do before the trick starts?")
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
        print("\nAlright first things first, pick a card by inputing a number betweet 1 and 52:")
        ans = input()
        while ans.strip().isdigit() == False or int(ans) <= 1 and int(ans) >= 52:
            ans = input("try again: ")
        


            
        

