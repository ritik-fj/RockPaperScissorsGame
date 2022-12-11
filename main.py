# Programmer: Ritik Kumar

import random

# Win count variables
player_win_count = 0
computer_win_count = 0

# Array containing all possible choices
options = ['Rock', 'Paper', 'Scissors']

# Game heading and instructions
print('==========================')
print('Rock, Paper, Scissors Game')
print('==========================')
print('- Type Rock, Paper, or Scissors to play with the computer\n'
      '- Type Q to quit the game\n')

while True:
    # Displays the win count of the player and computer
    print('--------------------')
    print('Player Wins = ', player_win_count, '\nComputer Wins = ', computer_win_count)
    print('--------------------')

    # Takes in the players choice
    user_choice = input('Your Choice: ').lower()

    # Ends the game
    if user_choice == 'q':
        print('Thank you for playing.')
        break

    # Generates a random number from 0 to 2
    rand_num = random.randint(0, 2)

    # Retrieves the computers choice from options array using the random number as the index
    computer_choice = options[rand_num]

    # Prints computers choice
    print('Computer Choice:', computer_choice)

    # All possible combinations and their outcomes
    # The win count of the player/computer gets incremented by 1 after each win
    if computer_choice == 'Rock' and user_choice == 'rock':
        print('DRAW!!!')
    elif computer_choice == 'Scissors' and user_choice == 'scissors':
        print('DRAW!!!')
    elif computer_choice == 'Paper' and user_choice == 'paper':
        print('DRAW!!!')
    elif computer_choice == 'Paper' and user_choice == 'rock':
        print('COMPUTER WINS!!!')
        computer_win_count += 1
    elif computer_choice == 'Paper' and user_choice == 'scissors':
        print('YOU WIN!!!')
        player_win_count += 1
    elif computer_choice == 'Rock' and user_choice == 'paper':
        print('YOU WIN!!!')
        player_win_count += 1
    elif computer_choice == 'Rock' and user_choice == 'scissors':
        print('COMPUTER WINS!!!')
        computer_win_count += 1
    elif computer_choice == 'Scissors' and user_choice == 'rock':
        print('YOU WIN!!!')
        player_win_count += 1
    elif computer_choice == 'Scissors' and user_choice == 'paper':
        print('COMPUTER WINS!!!')
        computer_win_count += 1
