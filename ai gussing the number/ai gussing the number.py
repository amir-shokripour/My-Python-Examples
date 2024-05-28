import random


def get_input(order):
    while True:
        user_input = input(order)
        return user_input


def range_of_guss():
    while True:
        the_start = get_input('enter the start point : ')
        the_end = get_input('enter the end point : ')

        if the_start.isdigit() and the_end .isdigit():
            return int(the_start), int(the_end)
        print('invalid input please enter number')
        print('*' * 30)


def user_choice(the_start, the_end):
    while True:
        print('*' * 30)
        the_answer = get_input(f'choose between {the_start} to {the_end} : ')
        if the_answer.isdigit():
            if the_start <= int(the_answer) <= the_end:
                return int(the_answer)
            else:
                print('*' * 30)
                print(f'the number must be betweeen {the_start} to {the_end}.')
        else:
            print('*' * 30)
            print('invalid input please enter a number')


def ai_guss(the_start, the_end):
    return random.sample(list(range(the_start, the_end)), 1)


def check_ai_guss(ai, the_start, the_end):
    while True:
        print('*' * 30)
        print(f'ai : the answer is {ai[0]}')
        res = get_input('t : True , g : greater , s : smaller : ')
        if res.lower().isalpha():
            if res == 't':
                print('😊')
                return
            elif res == 'g':
                the_start = ai[0]
                ai = ai_guss(the_start, the_end)
            elif res == 's':
                the_end = ai[0]
                ai = ai_guss(the_start, the_end)
        else:
            print('*' * 30)
            print('invalid input please try again.')


def start():
    the_start, the_end = range_of_guss()
    answer = user_choice(the_start, the_end)
    ai = ai_guss(the_start, the_end)
    check_ai_guss(ai, the_start, the_end)


start()
