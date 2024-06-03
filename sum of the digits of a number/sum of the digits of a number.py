def get_number():
    while True:
        number = input('Enter a number : ')
        if '.' in number:
            number = number.replace('.', '')
        if number.isdigit():
            return number
        print('Invalid input. Please enter a number')


def digits_sum():
    number = int(get_number())
    the_sum = 0
    while number > 0:
        units_digit = number % 10
        number //= 10
        the_sum += units_digit

    return the_sum


print(digits_sum())

# The second way


def digits_sum_2():
    number = get_number()
    the_sum = 0
    for digit in number:
        the_sum += int(digit)

    return the_sum


print(digits_sum_2())
