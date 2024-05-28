import random
import string
import os

settings = {
    'lower': True,
    'upper': True,
    'symbols': True,
    'number': True,
    'space': False,
    'lenght': 8
}

PASSWORD_MIN_LENGHT = 4
PASSWORD_MAX_LENGHT = 30


def clesr_screen():
    os.system('cls')


def get_user_password_lenght(option, defualt, pw_min_lenght=PASSWORD_MIN_LENGHT, pw_max_lengh=PASSWORD_MAX_LENGHT):
    while True:
        user_input = input(
            f'enter password lenght (Default is {defualt}) (enter : default) :')

        if user_input == '':
            return defualt

        if user_input.isdigit():
            user_pass_lenght = int(user_input)
            if pw_min_lenght <= user_pass_lenght <= pw_max_lengh:
                return user_pass_lenght
            print('Invalid input')
            print(
                f'password lenght shoud be between {pw_min_lenght} and {pw_max_lengh}')
        else:
            print('invalid input you should enter a number')
        print('please try again')


def change_setting_by_user(option, defualt):
    while True:
        user_input = input(
            f'Include {option} ? (Defualt is {defualt}) (yes : y , no : n , enter : defualt) : ')
        if user_input == '':
            return defualt

        if user_input in ['y', 'n']:
            return user_input == 'y'

        print('Invalid input! try again')


def get_settings_from_user(settings):
    for option, defualt in settings.items():
        if option != 'lenght':
            user_choice = change_setting_by_user(option, defualt)
            settings[option] = user_choice
        else:
            user_password_lenght = get_user_password_lenght(option, defualt)
            settings[option] = user_password_lenght


def ask_if_user_wants_to_change_settings(settings):
    while True:
        user_answer = input(
            'do you want to change the settings (y : yes , n : no , enter : yes) : ')

        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                print('-'*5, 'change settings', '-'*5, sep='')
                get_settings_from_user(settings)
            break
        else:
            print('Invalid input.')
            print('please try again')


def choose_lower_case():
    return random.choice(string.ascii_lowercase)


def choose_upper_case():
    return random.choice(string.ascii_uppercase)


def choose_number():
    return random.choice(string.digits)


def have_space():
    return ' '


def choose_symbols():
    return random.choice(string.punctuation)


def pass_maker(choices):
    choice = random.choice(choices)
    if choice == 'upper':
        return choose_upper_case()
    if choice == 'lower':
        return choose_lower_case()
    if choice == 'symbols':
        return choose_symbols()
    if choice == 'number':
        return choose_number()
    if choice == 'space':
        return have_space()


def ask_user_to_generate_another_password():
    while True:
        user_answer = input(
            'Regenerate the password ? (y : yes , n : no , enter : yes) : ')
        if user_answer in ['y', 'n', '']:
            if user_answer == 'n':
                return False
            return True
        else:
            print('Invalid input.')
            print('please try again')


def password_generator_loop(settings):
    while True:
        print('-'*20)
        print(f'generated password : {password_generator(settings)}')

        if ask_user_to_generate_another_password() == False:
            break


def password_generator(settings):
    password = ''
    password_lenght = settings['lenght']
    choices = list(filter(lambda x: settings[x], [
                   'lower', 'upper', 'symbols', 'number', 'space']))
    for i in range(password_lenght):
        password += pass_maker(choices)
    return password


def run_program():
    clesr_screen()
    ask_if_user_wants_to_change_settings(settings)
    password_generator_loop(settings)


run_program()
