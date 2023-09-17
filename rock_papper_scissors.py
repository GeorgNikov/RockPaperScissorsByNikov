import random
import os
os.system('color')

def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Choose [R]ock, [P]aper, [S]cissors: ')

if player_move == 'r' or player_move == 'R' or player_move == 'Rock' or player_move == 'rock':
    player_move = rock
elif player_move == 'p' or player_move == 'P' or player_move == 'Paper' or player_move == 'paper':
    player_move = paper
elif player_move == 's' or player_move == 'S' or player_move == 'Scissors' or player_move == 'scissors':
    player_move = scissors
else:
    print(colored(255, 0, 0,'Invalid Input. Try again... '))
    exit()


computer_random_number = random.randint(1, 3)
computer_move = ''

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

print(f'The computer chose {computer_move}.')

if player_move == computer_move:
    print(colored(0, 128, 255,'Draw'))
elif ((player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or
      (player_move == scissors and computer_move == paper)):
    print(colored(0, 255, 0, 'You win!'))
else:
    print(colored(255, 0, 0, 'You lose!'))
