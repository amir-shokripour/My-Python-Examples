def print_line_star(number_of_stars , total_stars):
    number_of_spaces = (total_stars - number_of_stars) // 2
    print(' '*number_of_spaces , end='')
    print('*'*number_of_stars , end='')
    print(' '*number_of_spaces)

def draw_diamond(num):
    print('-'*30)
    number_of_stars = None
    for i in range(num):
        if i < num /2:
            number_of_stars = i * 2 +1
        else:
            number_of_stars = (num-i)* 2 -1

        print_line_star(number_of_stars , num)

def user_input():
    num = int(input('enter an odd number : '))
    while num % 2 ==0:
        print('wrong input please enter an odd number')
        num = int(input('enter an odd number : '))

    return num

draw_diamond(user_input())