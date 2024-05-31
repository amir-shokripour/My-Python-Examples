def get_input(order):
    while True:
        num = input(order)
        if num.isdigit():
            return int(num)
        print('Invalid input please try again.')


def Perimeter_or_area():
    print('which operation do you want to use?\n1)Perimeter\n2)area')
    while True:
        user_choice = get_input('Enter the operation : ')
        if user_choice == 1:
            return 'Perimeter'
        elif user_choice == 2:
            return 'area'
        else:
            print('Invalid input please choose one of the valid options.')


def geometric_shapes():
    print('Please choose the shape :\n1)Square\n2)Rectangle\n3)Triangle\n4)Trapezoid\
          \n5)Rhombus/Diamond\n6)Parallelogram\n7)Circle')
    while True:
        user_choice = get_input('Enter your choice : ')
        print('*' * 30)
        if user_choice in range(1, 8):
            operation = Perimeter_or_area()
            return operation, user_choice
        print('Invalid input please choose one of the valid options.')


def square(operation):
    side_of_the_square = get_input('Enter side of the square : ')
    if operation == 'Perimeter':
        return f'Perimeter is : {side_of_the_square * 4}'
    return f'area is : {side_of_the_square **2}'


def rectangle(operation):
    length_of_the_rectangle = get_input('Enter length of the rectangle : ')
    the_width_of_the_rectangel = get_input(
        'Enter the width of the rectangel : ')
    if operation == 'Perimeter':
        return f'Perimeter is {(length_of_the_rectangle + the_width_of_the_rectangel) * 2}'
    return f'area is : {length_of_the_rectangle * the_width_of_the_rectangel}'


def triangle(operation):
    if operation == 'area':
        base = get_input('Enter the base : ')
        height = get_input('Enter the height : ')
        return f'area is : {(base * height) / 2}'
    side_a = get_input('Enter side a : ')
    side_b = get_input('Enter side b : ')
    side_c = get_input('Enter side c : ')
    return f'Perimeter is {side_a + side_b + side_c}'


def trapezoid(operation):
    base_a = get_input('Enter base a : ')
    base_b = get_input('Enter base b : ')
    if operation == 'area':
        height = get_input('Enter height : ')
        return f'area is : {(base_a + base_b) * height / 2}'
    side_c = get_input('Enter side c : ')
    side_d = get_input('Enter side d : ')
    return f'perimeter is : {side_c + side_d + base_a + base_b}'


def rhombus(operation):
    if operation == 'area':
        small_diagonal = get_input('Enter the small diagonal : ')
        great_diagonal = get_input('Enter the great diagonal : ')
        return f'area is : {small_diagonal * great_diagonal / 2}'
    side = get_input("Enter the side : ")
    return f'perimeter is : {side * 4}'


def parallelogram(operation):
    if operation == 'area':
        base = get_input('Enter the base : ')
        height = get_input('Enter the height : ')
        return f'area is : {base * height}'
    side_a = get_input('Enter side a : ')
    side_b = get_input('Enter side b : ')
    return f"perimeter is : {(side_a + side_b) * 2}"


def circle(operation):
    def pi():
        while True:
            pi_num = input('Enter π (3 or 3.14) : ')
            if pi_num == '3':
                return 3
            elif pi_num == '3.14':
                return 3.14
            print('Invalid input please enter π (3 or 3.14) : ')

    radius = get_input('Enter the radius : ')
    pi_num = pi()
    if operation == 'area':
        return f'area is : {radius**2 * pi_num}'
    return f'perimeter is : {2 * pi_num * radius}'


def run():
    operation, user_choice = geometric_shapes()
    if user_choice == 1:
        print(square(operation))
    elif user_choice == 2:
        print(rectangle(operation))
    elif user_choice == 3:
        print(triangle(operation))
    elif user_choice == 4:
        print(trapezoid(operation))
    elif user_choice == 5:
        print(rhombus(operation))
    elif user_choice == 6:
        print(parallelogram(operation))
    elif user_choice == 7:
        print(circle(operation))


run()


# Example
# Please choose the shape :
# 1)Square
# 2)Rectangle
# 3)Triangle
# 4)Trapezoid
# 5)Rhombus/Diamond
# 6)Parallelogram
# 7)Circle
# Enter your choice : 2
# ******************************
# which operation do you want to use?
# 1)Perimeter
# 2)area
# Enter the operation : 1
# Enter length of the rectangle : 10
# Enter the width of the rectangel : 6
# Perimeter is 32

# Please choose the shape :
# 1)Square
# 2)Rectangle
# 3)Triangle
# 4)Trapezoid
# 5)Rhombus/Diamond
# 6)Parallelogram
# 7)Circle
# Enter your choice : 4
# ******************************
# which operation do you want to use?
# 1)Perimeter
# 2)area
# Enter the operation : 1
# Enter base a : 8
# Enter base b : 5
# Enter side c : 4
# Enter side d : 4
# perimeter is : 21

# Please choose the shape :
# 1)Square
# 2)Rectangle
# 3)Triangle
# 4)Trapezoid
# 5)Rhombus/Diamond
# 6)Parallelogram
# 7)Circle
# Enter your choice : 7
# ******************************
# which operation do you want to use?
# 1)Perimeter
# 2)area
# Enter the operation : 2
# Enter the radius : 7
# Enter π (3 or 3.14) : 3.14
# area is : 153.86
