def get_nums():
    nums = []
    for i in range(3):
        if i == 0:
            var = 'first'
        elif i == 1:
            var = 'second'
        else:
            var = 'third'
        while True:
            num = input(f'enter {var} number : ')
            if num.isdigit():
                nums.append(int(num))
                break
            else:
                print('invalid input try again')
    return nums[0], nums[1], nums[2]


def check_if_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


def right_angled(a, b, c):
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return True
    return False


def equilateral_triangle(a, b, c):
    if a == b == c:
        return True
    return False


def isosceles_triangle(a, b, c):
    if a == b or b == c or a == c:
        return True
    return False


def result(a, b, c):
    if right_angled(a, b, c):
        return f'{a} ,{b} ,{c} makes right triangle'
    elif equilateral_triangle(a, b, c):
        return f'{a} ,{b} ,{c} makes equilateral triangle'
    elif isosceles_triangle(a, b, c):
        return f'{a} ,{b} ,{c} makes isosceles triangle'


def run():
    a, b, c = get_nums()
    res = check_if_triangle(a, b, c)
    if res:
        print(result(a, b, c))
    else:
        print(f'{a} ,{b} ,{c} cant make triangle.')


run()
