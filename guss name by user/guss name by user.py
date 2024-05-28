import random

names = ['shokripour', 'amiri', 'zare', 'hamidi', 'hosseini', 'dalaeli', 'ebrahimi', 'razi', 'latifi',
         'hajizade', 'salah', 'shojaei', 'alizade', 'mohammadi', 'naderi', 'parsayee', 'mohammadpour']


def play_again():
    while True:
        user_input = input(
            'Do you want to play again ? (y --> yes , n --> no) : ')
        if user_input in ['y', 'n']:
            if user_input == 'y':
                return True
            return False
        else:
            print('invalid input')


ai_choice = random.choice(names)

print('Welcome to the guss the name game')
print('if u needed help just enter help')
print('*'*10, 'here the names', '*'*10)

for number, name in enumerate(names):
    print(f'{number + 1} - {name}')

print('-' * 30)

user_guss = input(
    'Whats your guss? (enter the code of each name you guss is right) : ')
while True:
    if user_guss.isdigit() and int(user_guss) in list(range(len(names) + 1)):
        if names[int(user_guss) - 1] == ai_choice:
            print('you won!')
            if play_again():
                print('-' * 30)
                ai_choice = random.choice(names)
                user_guss = input(
                    'Whats your guss? (enter the code of each name you guss is right) : ')
            else:
                break

        else:
            print('-' * 30)
            print('wrong guss try again')
            user_guss = input(
                'Whats your guss? (enter the code of each name you guss is right) : ')

    elif user_guss.lower() == 'help':
        print('-' * 30)
        letters = []
        for i in ai_choice:
            letters.append(i)
        choosen_letter = random.choice(letters)
        letters.remove(choosen_letter)
        print(f'the ansewer include letter - {choosen_letter} - ')
        user_guss = input(
            'Whats your guss? (enter the code of each name you guss is right) : ')

    elif user_guss == 'exit':
        break
    else:
        print('-' * 30)
        print('invalid input please try again')
        user_guss = input(
            'Whats your guss? (enter the code of each name you guss is right) : ')
