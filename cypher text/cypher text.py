

def get_input(order):
    return input(order)


def get_digit(order):
    while True:
        num = get_input(order)
        if num.isdigit():
            return int(num)
        print('invalid input')


def chosse_the_operation():
    print('*' * 20, 'choose the operation', '*' * 20)
    print('1)convert text to cypher\n2)convert cypher to the text\n3)exit')
    while True:
        user_input = get_input('which operation do you want to use ? : ')
        if user_input.isdigit():
            if int(user_input) in [1, 2, 3]:
                return int(user_input)
            else:
                print('invalid input')
        else:
            print('you must enter a number')


def user_choice(operation):
    if operation == 1:
        return f'Encrypted text: {encrypt()}'
    elif operation == 2:
        return f"Decrypted text: {decrypt()}"
    else:
        return 'bye'


def encrypt():
    plain_text = get_input('Enter plain text : ')
    key = get_digit('enter the key : ')
    cypher_text = ''
    for ch in plain_text:
        cypher_text += chr(ord(ch) + key)
    return cypher_text


def decrypt():
    cypher_text = get_input('Enter cypher text : ')
    key = get_digit('enter the key : ')
    plain_text = ''
    for ch in cypher_text:
        plain_text += chr(ord(ch) - key)
    return plain_text


def run():
    while True:
        operation = chosse_the_operation()
        result = user_choice(operation)
        print(result)
        if operation == 3:
            break


run()


# Example
# ******************** choose the operation ********************
# 1)convert text to cypher
# 2)convert cypher to the text
# 3)exit
# which operation do you want to use ? : 1
# Enter plain text : a bird on the tree
# enter the key : 4
# Encrypted text: e$fmvh$sr$xli$xvii
# ******************** choose the operation ********************
# 1)convert text to cypher
# 2)convert cypher to the text
# 3)exit
# which operation do you want to use ? : 2
# Enter cypher text : e$fmvh$sr$xli$xvii
# enter the key : 4
# Decrypted text: a bird on the tree
# ******************** choose the operation ********************
# 1)convert text to cypher
# 2)convert cypher to the text
# 3)exit
# which operation do you want to use ? : 3
# bye
