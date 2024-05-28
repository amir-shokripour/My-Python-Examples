import random


def get_input(order):
    while True:
        user_input = input(order)
        if user_input.isdigit():
            return int(user_input)
        print('invalid input please enter a number')


def get_the_start_and_the_end():
    start_point = get_input('enter the start range : ')
    end_point = get_input('enter the end range : ')
    return start_point, end_point


def user_guss(start_point, end_point, ai):
    print(f'guss between {start_point} to {end_point}')

    while True:
        user_gussing = get_input('Enter your guss : ')

        if start_point <= user_gussing <= end_point:

            if user_gussing == ai:
                print('correct')
                return
            elif user_gussing > ai:
                print('*' * 30)
                print('wrong!')
                print('the answer is smaller than your guss')
            else:
                print('*' * 30)
                print('wrong!')
                print('the answer in greater than your guss')
        else:
            print('*' * 30)
            print('your guss in out of range please try again.')


def ai_choice(start_point, end_point):
    ai = random.randint(start_point, end_point)
    return ai


def start():
    start_point, end_point = get_the_start_and_the_end()
    print('*' * 30)
    ai = ai_choice(start_point, end_point)
    user_guss(start_point, end_point, ai)


start()
