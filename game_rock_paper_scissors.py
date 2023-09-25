import random
import time

# set two global variables to count the current score
CURRENT_WINS_PLAYER = 0
CURRENT_WINS_COMPUTER = 0

print()
print('\x1b[48;5;237m\x1b[38;5;14mWelcome to the Rock, Paper, Scissors Game! \033[0;0m')

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
starting_title = 'Welcome to the Rock, Paper, Scissors Game!'
player_move_text = 'Choose [r]ock, [p]aper or [s]cissors: '


time.sleep(2)

# check for valid input for the number of turns
while True:
    try:
        print('\x1b[38;5;225m')
        turns = int(input('Best out of (3 or 5): '))
        if turns == 3 or turns == 5:
            break
        continue
    except ValueError:
        print('Invalid input. Please try again.')

# check when a player has won the final game
necessary_wins = int(turns / 2) + 1


while True:
    print('\x1b[38;5;225m')
    player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

    if player_move == 'Q':
        print('Thank you for playing.')
        break

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid Input. Try again...')

    computer_random_number = random.randint(1, 3)
    computer_move = ''

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f'The computer chose {computer_move}.')

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print('\x1b[38;5;11mYou won the current match!')
        CURRENT_WINS_PLAYER += 1
    elif player_move == computer_move:
        print('Draw!')
    else:
        print('You lost the match.')
        CURRENT_WINS_COMPUTER += 1

    if CURRENT_WINS_PLAYER == necessary_wins or CURRENT_WINS_COMPUTER == necessary_wins:
        break
    print('\x1b[38;5;38m')
    print(f'Type \'Q\' if you want to exit the game !')

if CURRENT_WINS_PLAYER > CURRENT_WINS_COMPUTER:
    print('\x1b[38;5;48m')
    print('Congratulations! You won the game !')
else:
    print('Oh,no. The Computer won the game')
print(f'You scored: {CURRENT_WINS_PLAYER} point(s)!')

