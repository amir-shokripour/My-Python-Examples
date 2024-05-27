import random


def get_user_input(prompt):
    while True:
        user_input = input(prompt)

        if user_input.isdigit():
            return int(user_input)
        print('Invalid input! Please enter a valid number.')
        print('-'*20)


def chances_and_cups():
    print("Welcome to the Gussing game")
    chances = get_user_input('Enter number of chances: ')
    cups = get_user_input('Enter number of cups: ')
    return chances, cups


def ai_choice(cups):
    return random.randint(2, cups)


def user_gess(cups):
    while True:
        guss = get_user_input(f'What is your guss ? [1 to {cups}] : ')

        if 1 <= guss <= cups:
            return guss
        print('Invalid input! Please enter a number within the specified range')
        print('-'*20)


def check_guss(ai, user_guss_value):
    return user_guss_value == ai


def result(res):
    if res:
        return 'congratulations! You won!'
    else:
        return 'Wronge guss. try again.'


def game():
    chances, cups = chances_and_cups()
    ai = ai_choice(cups)

    for chance in range(chances, 0, -1):
        print('-'*20)
        print(f'{chance} {"chances" if chance > 1 else "chance"} left')

        user_guss_value = user_gess(cups)
        res = check_guss(ai, user_guss_value)
        print(result(res))

        if res:
            return

    print('-'*20)
    print(f'The correct answer was {ai}. YOU LOST')


game()
