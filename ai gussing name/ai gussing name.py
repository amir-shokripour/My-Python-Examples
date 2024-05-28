import random

names = ['shokripour', 'amiri', 'zare', 'hamidi', 'hosseini', 'dalaeli', 'ebrahimi', 'razi', 'latifi',
         'hajizade', 'salah', 'shojaei', 'alizade', 'mohammadi', 'naderi', 'parsayee', 'mohammadpour']


def the_names(names):
    for index, name in enumerate(names, start=1):
        print(f'{index} - {name}')


def user_choice(names):
    while True:
        user_input = input('enter the code of the name you choosed : ')
        if user_input.isdigit() and names[int(user_input) - 1] in names:
            return names[int(user_input) - 1]


def ai_guss(names):
    return random.choice(names)


def check_the_guss(names, ai_choice):
    while True:
        print(f'ai guss is : {ai_choice}')

        user_input = input('ai gussed right ? (y/n) :')
        if user_input == 'y':
            return '😊'
        elif user_input == 'n':
            print('*' * 30)
            names.remove(ai_choice)
            ai_choice = ai_guss(names)
        else:
            print('invalid input please enter (y/n)')


def start(names):
    print('chosse a name please')
    print('*' * 30, 'here the names', '*' * 30)
    the_names(names)
    ansewer = user_choice(names)
    print(f'the ansewr is {ansewer}')
    print('*' * 30)
    ai_choice = ai_guss(names)
    print(check_the_guss(names, ai_choice))


start(names)
