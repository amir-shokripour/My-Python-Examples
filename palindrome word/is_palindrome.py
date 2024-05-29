def is_palindrome(word, reversed_word):
    if word == reversed_word:
        return 'palindrome'
    return 'not palindrome'


def get_input():
    while True:
        word = input('Please enter a word : ')
        if word.isalpha():
            reversed_word = word[::-1]
            return is_palindrome(word, reversed_word)
        print('Invalid input please try again.')


print(get_input())
