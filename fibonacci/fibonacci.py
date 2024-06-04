def num():
    while True:
        number = input('Enter a number : ')
        if number.isdigit():
            return int(number)
        print('Invalid input please try again.')


def fibonacci():
    number = num()
    a, b = 0, 1
    for i in range(number):
        print(b)
        a, b = b, a + b


fibonacci()

# The second way


def fibonacci_2(number):
    if number == 1 or number == 0:
        return 1
    return fibonacci_2(number - 1) + fibonacci_2(number - 2)


for number in range(1, num()):
    print(fibonacci_2(number))


# Example

# Enter a number : 10
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

# The second way
# Enter a number : 10
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
