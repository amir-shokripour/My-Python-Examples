import random

choices = ['r', 'p', 's']
choices_meaning = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}


def get_rounds():
    while True:
        rounds = input('enter how many rounds do you want to play ? ')
        print('-'*20)

        if rounds.isdigit():
            return int(rounds)

        print('invalid input! please try again.')
        print('-'*20)


def get_ai_choice(choices):
    ai_choice = random.choice(choices)
    return ai_choice


def get_user_choice(choices):
    while True:
        user_choice = input(
            'enter your choice ? (r : rock, p : paper , s : scissors) : ')

        if user_choice in choices:
            return user_choice

        print('invalid input! please try again.')
        print('-'*20)


def play_the_game(choices_meaning, choices):
    ai_score = 0
    user_score = 0

    for round in range(get_rounds()):

        ai_choice = get_ai_choice(choices)
        user_choice = get_user_choice(choices)

        print(
            f'your choice is {choices_meaning[user_choice]} and ai choice is {choices_meaning[ai_choice]}')

        if ai_choice == user_choice:
            print('tie')
            print('-'*20)
        elif (user_choice == 'r' and ai_choice == 's') or (user_choice == 'p' and ai_choice == 'r') or (user_choice == 's' and ai_choice == 'p'):
            user_score += 1
            print(
                f'user score +1 , your score : {user_score} and ai score : {ai_score}')
            print('-'*20)
        else:
            ai_score += 1
            print(
                f'ai score +1 , ai score : {ai_score} and your score : {user_score}')
            print('-'*20)

    return ai_score, user_score


def result(choices_meaning, choices):
    ai_score, user_score = play_the_game(choices_meaning, choices)

    if ai_score == user_score:
        print('its a tie')
    elif ai_score > user_score:
        print(f'ai won with score : {ai_score}')
    else:
        print(f'you won with score : {user_score}')


result(choices_meaning, choices)
