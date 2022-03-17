# By Ethan Wong
# 17 March 2022 10:40pm
"""
This code is full of bugs and errors, and does not currently work.
"""


import random


def welcome():
    print("Welcome to Paper Scissors Rock! A game of chance? A game of strategy? A reward if you do, but you won't defeat me!")
    print("=============================================")


def ask_player():
    print()
    answer = input("Choose: \n 'paper',\n 'scissors', \n 'rock' >>> ").lower()
    while answer != "paper" and answer != "scissors" and answer != "rock":
        print()
        answer = input("Invalid answer! \nChoose: \n 'paper',\n 'scissors', \n 'rock' >>> ").lower()

    return answer


def computer_answer():
    option = random.randint(1, 3)
    if option == 1:
        answer = "paper"
    elif option == 2:
        answer = "scissors"
    elif option == 3:
        answer = "rock"
    else:
        print("Something went wrong")
    print(f"I chose: {answer}")
    return answer


def play_game():
    player = ask_player()
    #print(player)
    computer = computer_answer()
    #print(computer)

    if player == computer:
        print(f"Tie! We both chose {player.capitalize()}")
        return "tie"

    # figuring out winner logic
    elif player == "paper":
        if computer == "rock":
            return "player"
        else:
            return "computer"
    elif player == "scissors":
        if computer == "paper":
            return "player"
        else:
            return "computer"
    elif player == "rock":
        if computer == "scissors":
            return "player"
        else:
            return "computer"
    else:
        return "error"


# main routine
welcome()
player_name = input("What is your name >>> ")
print(f"Hello, {player_name.capitalize()}")

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    winner = play_game()
    if winner == "player":
        print("You win this round!")
        player_score += 1
    elif winner == "computer":
        print("I win this round!")
        computer_score += 1

    print(f"{player_score} - {computer_score}")

    play_game()

print(f"The score was {player_score} - {computer_score}")
if player_score > computer_score:
    print("You win.")
else:
    print("I win! Better luck next time, chump")
