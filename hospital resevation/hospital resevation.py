import random


with open('datafile.txt', 'a') as file:

    user = input('start the program (y --> yes and n --> no) : ')
    while user != 'exit':
        data = {}
        if user.isalpha() and user == 'y':

            def ask_users_perpose():
                print('Hi , wellcome to the resevation visites of hospital')
                user_input = input(
                    'Do you want to reserve a visite time? (y --> yes and n --> no) :').lower()
                while True:
                    if user_input in ['y', 'n']:
                        if user_input == 'y':
                            return True
                        print('good, now Do not distrup!! go home.')
                        return False
                    else:
                        print('invalid input, please try again.')
                        print('-' * 30)
                        user_input = input(
                            'Do you want to reserve a visite time? (y --> yes and n --> no) :').lower()

            def present_sections():
                sections = ['general practitioner',
                            'internist', 'dental', 'ophthalmology']
                print('-' * 30)
                print('please choose the section')
                for num, section in enumerate(sections):
                    print(f'{num + 1} - {section}')
                return sections

            def ask_for_section(sections):
                user_input = input('Enter the code of section (1 to 4) : ')
                while True:
                    if user_input.isdigit() and int(user_input) in [1, 2, 3, 4]:
                        print('-' * 30)
                        print(
                            f'you choosed {sections[int(user_input) - 1]} section.')
                        return sections[int(user_input) - 1]
                    print('invalid input Please try again.')
                    print('-' * 30)
                    user_input = input('Enter the code of section (1 to 4) : ')

            def choose_time(times):
                for num, time in enumerate(times):
                    print(f'{num + 1} - {time}')

                time_input = input('please enter the code of time : ')
                while True:
                    if time_input.isdigit() and int(time_input) in list(range(1, len(times) + 1)):
                        return times[int(time_input) - 1]
                    print('-' * 30)
                    print('invalid input please try again')
                    time_input = input('please enter the code of time : ')

            def ask_the_day(choosen_section):
                print('now choose the day.')
                times = [['8am', '8:30am', '9am', '9:30am', '10am', '10:30am', '11am', '11:30am', '12pm', '12:30pm', '1pm', '1:30pm'],
                         ['2pm', '2:30pm', '3pm', '3:30pm', '4pm', '4:30pm', '5pm', '5:30pm', '6pm', '6:30pm', '7pm', '7:30pm', '8pm', '8:30pm', '9pm', '9:30pm', '10pm']]

                days_of_each_section = {
                    'general practitioner': {
                        'saturday': times[0],
                        'sunday':  times[1],
                        'monday':  times[0],
                        'tuseday':  times[1],
                        'wenseday':  times[0],
                        'thursday':  times[1]
                    },

                    'internist': {
                        'saturday': times[1],
                        'monday':  times[0],
                        'wenseday':  times[1]
                    },

                    'dental': {
                        'sunday':  times[1],
                        'tuseday':  times[0],
                        'thursday':  times[0]
                    },

                    'ophthalmology': {
                        'sunday':  times[0],
                        'monday':  times[0],
                        'wenseday':  times[1]
                    }
                }

                i = 0
                for _ in days_of_each_section[choosen_section]:
                    i += 1
                    print(f'{i} - {_}')

                day_input = input('please enter the code of the day : ')
                print('-' * 30)
                while True:
                    if day_input.isdigit() and int(day_input) in list(range(1, len(days_of_each_section[choosen_section]) + 1)):
                        the_day = list(
                            days_of_each_section[choosen_section].keys())
                        time = days_of_each_section[choosen_section][the_day[int(
                            day_input) - 1]]
                        return choose_time(time), the_day[int(day_input) - 1]
                    else:
                        print('-' * 30)
                        print('invalid input please try again')
                        day_input = input(
                            'please enter the code of the day : ')

            def fullname():
                print('-' * 30)
                firstname = input('please enter your firstname : ')
                lastname = input('please enter your lastname : ')
                while True:
                    if firstname.replace(' ', '').isalpha() and lastname.isalpha():
                        return firstname.title(), lastname.title()
                    print('-' * 30)
                    print('invalid input please try again')
                    firstname = input('please enter your firstname : ')
                    lastname = input('please enter your lastname : ')

            def creat_receipt_number(data):
                num = random.randint(1000, 999999)
                while True:
                    if num in data:
                        num = random.randint(1000, 999999)
                        return num
                    return num

            def run(data):
                users_perpose = ask_users_perpose()
                if users_perpose:
                    sections = present_sections()
                    choosen_section = (ask_for_section(sections))
                    time, day = ask_the_day(choosen_section)
                    firstname, lastname = fullname()
                    receipt_num = creat_receipt_number(data)
                    if receipt_num in data:
                        receipt_num = creat_receipt_number(data)

                data[receipt_num] = [firstname,
                                     lastname, choosen_section, day, time]

            run(data)
            res = str(data.items())
            file.write(f'\n{res}')

        elif user == 'n':
            break

        else:
            print('Invalid input please try again')

        user = input(
            'do you wan to run the program again (y --> yes and n --> no) :')
