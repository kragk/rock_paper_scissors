# rock_paper_scissors
import random

def cpu_choose(choice):
    return choose(choice)

def choose(choice):
    if choice == 0:
        return 'rock'
    elif choice == 1:
        return 'paper'
    else:
        return 'scissors'

def player_winner(player, cpu):
    if player == cpu:
        return 0 # 0 = TIE
    elif (player == 'rock' and cpu == 'scissors') \
    or (player == 'scissors' and cpu == 'paper')\
    or (player == 'paper' and cpu == 'rock'):
        return 1 # 1 = WIN
    return 2 # 2 = LOSE

rounds = 3
player_score = 0
cpu_score = 0

while rounds != 0:
    rps_sequence = []
    rps_sequence.append(cpu_choose(random.randint(0,2)))
    rps_sequence.append(input('Rock, paper, or scissors: '))
    if rps_sequence[-1] not in ['rock','paper','scissors']:
        print('You did not input rock, paper, or scissors.')
        continue
    win_var = player_winner(rps_sequence[-1], rps_sequence[0])
    if win_var == 0:
        print('Tie!')
        continue
    elif win_var == 1:
        print('You win this round!')
        player_score += 1
    elif win_var == 2:
        print('You lose this round!')
        cpu_score += 1
    rounds -= 1

if player_score > cpu_score:
    print('You win the game!')
else:
    print('You lose the game!')
