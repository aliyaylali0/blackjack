import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
user_score = 0
computer_cards = []
computer_score = 0
player_new_card = False
computer_new_card = False
game = True
def deal_card():

    if player_new_card == True:
        user_cards.append(random.choice(cards))
        

    if player_new_card == False:
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))

        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    if computer_new_card == True:
        computer_cards.append(random.choice(cards))


def calculate_score():
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    if user_score == 21:
        print("You win")
        game = False
    elif computer_score == 21:
        print("computer win")
        game = False

    if user_score > 21:
        print("You lost")
        game = False
    elif computer_score > 21:
        print("computer lose")
        game = False

    if computer_score < 17:
        computer_new_card = True

    if user_score > computer_score:
        print("You win")
    elif user_score == computer_score:
        print("draw")


    print(f"user score: {user_score}")




while game:

    blackjack = input("Do you want to play blackjack 'y' or 'n': ").lower()

    if blackjack == 'y':

        deal_card()
        calculate_score()
        print(user_cards)
        print(f"computer first card:{computer_cards[0]}")

        new_card = input("Type 'y' get another new card, type 'n' pass: ")

        if new_card == 'y':
            player_new_card = True

        elif new_card == 'n':
            calculate_score()

    elif blackjack == 'n':
        game = False

