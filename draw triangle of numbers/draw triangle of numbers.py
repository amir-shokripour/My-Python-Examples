def get_num():
    while True:
        num = input('Enter a number : ')
        if num.isdigit():
            return int(num)
        print('Invalid input. Please try again.')


def draw_triangle():
    num = get_num()
    for i in range(1, num + 1):
        for j in range(1, num - i + 1):
            print(end=' ')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


draw_triangle()
