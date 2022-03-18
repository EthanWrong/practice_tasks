"""Paper, Scissors, Rock
By Ethan Wong
18 March 2022 3:46pm
"""

import random


def get_player_name():
    name = input("What is the name of the fool who dares to challenge me? ").capitalize()
    return name


def get_player_guess():
    print("--------------------")
    guess = input("Shoot: ").lower()
    while not guess in ("paper", "scissors", "rock"):
        guess = input("That's not a real option, cheater. \n You can choose 'paper', 'scissors', or 'rock'\nShoot: "
                      "").lower()
    return guess


def get_computer_guess():
    option = random.randint(1, 3)
    if option == 1:
        guess = "paper"
    elif option == 2:
        guess = "scissors"
    else:
        guess = "rock"
    print(f"I chose *{guess}*")
    return guess


def determine_winner(player, computer):
    print()
    if player == computer:
        print(f"We both chose {player}, tie")
        return "tie"
    elif player == "paper" and computer == "rock":
        print(f"{player.capitalize()} beats {computer}, you win. Witchcraft, no doubt")
        return "player"
    elif player == "scissors" and computer == "paper":
        print(f"{player.capitalize()} beats {computer}, you win. Mere luck")
        return "player"
    elif player == "rock" and computer == "scissors":
        print(f"{player.capitalize()} beats {computer}, you win. How can this be?!")
        return "player"
    else:
        print(f"{computer.capitalize()} beats {player}, I win (just as I expected)")
        return "computer"


def play_game():
    player_score = 0
    computer_score = 0
    name = get_player_name()

    # plays until someone gets to 3
    while player_score < 3 and computer_score < 3:
        player = get_player_guess()
        computer = get_computer_guess()
        winner = determine_winner(player, computer)
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        print(f"{player_score} - {computer_score}")

    print()
    if player_score > computer_score:
        print(f"You won, {name}! Savour the moment for it will not happen again")
    else:
        print(f"I win the contest! You are weak, {name}")
        print()
        print("\n            (O)\n            <M\n o          <M  THERE CAN BE ONLY ONE!!!\n/| ......  "
              "/:M\------------------------------------------------,,,,,,\n(O)[]XXXXXX[]I:K+}=====<{H}>================================------------>\n\| ^^^^^^  \:W/------------------------------------------------''''''\n o          <W  Artwork By Ian Broverman\n            <W\n            (O)")


print("Welcome to Paper, Scissors, Rock. \nNo doubt you will crumble in the face of my strength")
print("===================================================================")
play_game()
