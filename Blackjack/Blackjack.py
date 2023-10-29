import random
import os
import Blackjack_Art

# Starting money, cards & setting blackjack initially to no.

starting_money = 100
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Blackjack = "no"
want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# Keep playing as long as user types "y". Giving user two cards & computer one and adding user cards.

while want_to_play == "y":
    your_cards = []
    computer_cards = []

    for i in range(0,2):
        your_cards.append(random.choice(cards))

    computer_first_card = random.choice(cards)
    computer_cards.append(computer_first_card)
    first_sum = sum(your_cards)

    # Display logo, provide starting money, asking how much to bet. Letting user know cards, score & computer card.

    print(Blackjack_Art.logo)
    print(f"Your starting money is: £{starting_money}")
    bet = int(input("How much do you want to bet: £ "))
    print(f"Your cards: {your_cards}, current score: {first_sum}")
    print(f"Computer's first card: {computer_first_card}")

    # Letting user know if they have Blackjack. Asking if they want another card.

    if 11 in your_cards and 10 in your_cards:
        Blackjack = "yes"
        print("Blackjack!")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    # If yes to card, add card then sum up cards. If sum > 21 and no 11(ace), user bust and loses bet.
    # If sum > 21 and 11 in cards, switch 11 to 1 and sum. Then print cards. Also do this if < 21.

    while another_card == "y":
        your_cards.append(random.choice(cards))
        total_sum = sum(your_cards)
        if total_sum > 21 and 11 not in your_cards:
            print(f"Your cards: {your_cards}, current score: {total_sum}")
            print("You bust")
            starting_money -= bet
            break
        elif total_sum > 21 and 11 in your_cards:
            target_index = your_cards.index(11)
            your_cards[target_index] = 1
            total_sum = sum(your_cards)
            print(f"Your cards: {your_cards}, current score: {total_sum}")
            print(f"Computer's first card: {computer_first_card}")
        else:
            print(f"Your cards: {your_cards}, current score: {total_sum}")
            print(f"Computer's first card: {computer_first_card}")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        # Function to call when computer's cards over 17. Checks different end conditions then prints result.

    def is_over_17():
        global starting_money
        if sum(computer_cards) > sum(your_cards):
            print("Computer wins")
            starting_money = starting_money - bet
            another_card = "No"
        elif sum(computer_cards) < sum(your_cards):
            print("You win")
            if Blackjack == "yes":
                starting_money = starting_money +(bet *1.5)
                another_card = "No"
            else:
                starting_money = starting_money + bet
                another_card = "No"
        else:
            if Blackjack == "yes" and len(computer_cards) > 2:
                print("You win")
                starting_money = starting_money +(bet *1.5)
                another_card = "No"
            else:
                print("It is a draw")
                another_card = "No"

    # If user doesn't take another card, computer takes cards until > 17 or bust.

    while another_card == "n":
        computer_cards.append(random.choice(cards))
        total_sum2 = sum(computer_cards)
        if total_sum2 > 21:
            if total_sum2 > 21 and 11 not in computer_cards:
                print(f"Computer's cards are: {computer_cards}, current score: {total_sum2}")
                print("computer bust")
                print("You win")
                if Blackjack == "yes":
                    starting_money = starting_money + bet *1.5
                else:
                    starting_money += bet
                break
            elif total_sum2 > 21 and 11 in computer_cards:
                target_index2 = computer_cards.index(11)
                computer_cards[target_index2] = 1
                total_sum2 = sum(computer_cards)
        if total_sum2 >= 17:
            is_over_17()
            print(f"Computer's cards are: {computer_cards}, current score: {total_sum2}")
            break
    if starting_money <= 0:
        want_to_play = "NO"
        print("You have run out of money")
    else:
        want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        os.system("cls")



        

        

