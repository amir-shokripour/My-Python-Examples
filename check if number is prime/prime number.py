def get_number_from_user():
    while True:
        user_input = input('enter a number : ')

        if user_input.isdigit():
            return int(user_input)
        print('invalid input! please try again.')


def check_if_num_is_prime():
    num = get_number_from_user()
    if num == 1:
        return '1 is not a composite or prime number'
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return f'{num} is not prime'
    return f'{num} is prime'


print(check_if_num_is_prime())
