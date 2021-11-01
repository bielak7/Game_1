# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random

user_wins = 0
computer_wins =0

options = ["rock", "paper", "scissors"]
options[0]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

        #kamień: 0, papier:1,
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
         print("You won!")
         user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
         print("You won!")
         user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
         print("You won!")
         user_wins += 1

    else:
         print("You lost")
         computer_wins += 1

print("You won", user_wins, "times.")
print("the computer won", computer_wins, "times")
print("Goodbay!")
