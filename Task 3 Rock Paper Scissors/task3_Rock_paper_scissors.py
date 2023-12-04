# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:21:01 2023

@author: PC-5
"""
'''
#       Rock Paper Scissors
import random


# o =Rock
# 1 = Paper
# 2 = Scissors



user_choice = int( input("Enter your choice: Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors : "))

if user_choice >=  3 or user_choice < 0:
    print('Invalid Number')
else:
    
    computer_choice = random.randint(0,2)
    
    print ("Computer Choice",computer_choice)
    
    if computer_choice == user_choice:
        print('It is Draw')
    elif computer_choice == 0 and user_choice == 2:
        print('You lose')
    elif user_choice == 0 and computer_choice ==2:
        print('You win')
    elif computer_choice > user_choice:
        print('You Lose')
    elif user_choice > computer_choice:
        print('You Win')
'''

import random

print('Welcome to the Rock Paper Scissors Game...!!!\n')

# Setting win counters for both player and computer
player_wins = 0
computer_wins = 0

# Running the game using a while loop
while True:
    # Player inputs their choice
    player = input("Enter a choice (rock, paper, scissors): ")
    
    # List of possible choices
    choices = ["rock", "paper", "scissors"]
    
    # Computer randomly selects its choice
    computer = random.choice(choices)
    print(f"\nYou chose {player}, computer chose {computer}.")

    # Game logic to determine the winner
    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors. You win!")
            player_wins += 1
        else:
            print("Paper covers rock. You lose.")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock. You win!")
            player_wins += 1
        else:
            print("Scissors cut paper. You lose.")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cut paper. You win!")
            player_wins += 1
        else:
            print("Rock smashes scissors. You lose.")
            computer_wins += 1

    # Displaying the current score
    print("You have " + str(player_wins) + " wins")
    print("The computer has " + str(computer_wins) + " wins")
    
    # Asking if the player wants to play again
    repeat = input("\nPlay again? (yes/no): ")
    if repeat.lower() != "yes":
        print("Thanks for playing!")
        break  # Exit the loop if the player does not want to play again
