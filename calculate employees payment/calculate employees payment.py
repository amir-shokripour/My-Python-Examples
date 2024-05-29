def ask_for_info():
    while True:
        user_input = input(
            'Do you want to fill the payment information (y : yes , n : no , enter : yes) : ')

        if user_input in ['y', 'n', '']:
            if user_input == 'n':
                return False
            return True

        else:
            print('invalid input please try again')
            print('-'*30)


def get_name():
    while True:
        name = input('enter name : ')
        if name.isalpha():
            return name
        else:
            print('invalid input please try again')
            print('-'*30)


def get_hours_of_work():
    while True:
        hours_of_work = input('enter hours of work : ')
        if hours_of_work.isdigit():
            return int(hours_of_work)
        else:
            print('invalid input please try again')
            print('-'*30)


def get_pay_per_hour():
    while True:
        pay_per_hour = input('enter pay per hour : ')
        if pay_per_hour.isdigit():
            return int(pay_per_hour)
        else:
            print('invalid input please try again')
            print('-'*30)


def get_over_time():
    while True:
        over_time = input('enter over time : ')
        if over_time.isdigit():
            return int(over_time)
        else:
            print('invalid input please try again')
            print('-'*30)


def get_over_time_payment():
    while True:
        over_time_payment = input('enter over time payment : ')
        if over_time_payment.isdigit():
            return int(over_time_payment)
        else:
            print('invalid input please try again')
            print('-'*30)


def get_info():

    pay_info = {}

    pay_info['name'] = get_name()
    pay_info['hours_of_work'] = get_hours_of_work()
    pay_info['pay_per_hour'] = get_pay_per_hour()
    pay_info['over_time'] = get_over_time()
    pay_info['over_time_payment'] = get_over_time_payment()

    return pay_info


def info(all_info):
    pay_info = get_info()
    all_info.append(pay_info)


def calc_payment(all_info):
    for person in all_info:
        payment = (person['hours_of_work'] * person['pay_per_hour']) + \
            (person['over_time'] * person['over_time_payment'])
        print(f"{person['name']} : {payment} $")


def run():
    all_info = []
    res = ask_for_info()
    while res:
        info(all_info)
        res = ask_for_info()
    calc_payment(all_info)


run()

# Example
# Do you want to fill the payment information (y : yes , n : no , enter : yes) : y
# enter name : amir
# enter hours of work : 60
# enter pay per hour : 22
# enter over time : 5
# enter over time payment : 24
# Do you want to fill the payment information (y : yes , n : no , enter : yes) : pressed enter key
# enter name : david
# enter hours of work : 50
# enter pay per hour : 22
# enter over time : 10
# enter over time payment : 24
# Do you want to fill the payment information (y : yes , n : no , enter : yes) : n
# amir : 1440 $
# david : 1340 $
