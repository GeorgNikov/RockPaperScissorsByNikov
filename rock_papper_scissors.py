import random


def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
quit_program = 'Quit'
my_pts = 0
computer_pts = 0

player_move = input('Choose [R]ock, [P]aper, [S]cissors or [Q]uit: ')

while player_move != 'Quit':

    if player_move == 'r' or player_move == 'R' or player_move == 'Rock' or player_move == 'rock':
        player_move = rock
    elif player_move == 'p' or player_move == 'P' or player_move == 'Paper' or player_move == 'paper':
        player_move = paper
    elif player_move == 's' or player_move == 'S' or player_move == 'Scissors' or player_move == 'scissors':
        player_move = scissors
    elif player_move == 'q' or player_move == 'Q' or player_move == 'Quit' or player_move == 'quit':
        print(colored(0, 255, 0, 'Good bye...'))
        player_move = quit_program
        break
    else:
        print(colored(255, 0, 0, 'Invalid Input. Try again... '))
        break

    print(f'You chose {colored(255, 140, 0, player_move)}.')

    computer_random_number = random.randint(1, 3)
    computer_move = ''

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f'The computer chose {colored(255, 140, 0, computer_move)}.')

    if player_move == computer_move:
        print(colored(0, 128, 255, 'Draw'))
    elif ((player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or
          (player_move == scissors and computer_move == paper)):
        my_pts += 1
        print(colored(0, 255, 0, 'You win!'))
    else:
        print(colored(255, 0, 0, 'You lose!'))
        computer_pts += 1
    print()
    print(colored(238, 130, 238, f'Score: You {my_pts} - PC {computer_pts}'))
    player_move = input('Choose [R]ock, [P]aper, [S]cissors, [Q]uit: ')
