import random
list_of_words = ['css', 'java', 'python', 'amir']


def no_repeated_letters(list_of_words):
    while True:
        word = random.choice(list_of_words)

        if len(set(word)) == len(word):
            return (''.join(word))


print(no_repeated_letters(list_of_words))
