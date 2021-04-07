#---Rock Paper Scissors----#

import random
player1_action=input("paper,rock,scissors select one")
player2_action=random.choice(player1_action)
if player1_action == player2_action:
    print(f"Both players selected {player1_action}. It's a tie!")
elif player1_action == "rock":
    if player2_action == "scissors":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! You lose.")
elif player1_action == "paper":
    if player2_action == "rock":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! You lose.")
elif player1_action == "scissors":
    if player2_action == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("Rock beats scissors! You lose.")
