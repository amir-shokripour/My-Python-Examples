# ord()
# text to Unicode

def get_text():
    while True:
        text = input('Enter the text : ')
        if all(char.isalpha() or char.isspace() for char in text):
            return text
        print('Invalid input.Please try again.')


def convert_to_ord():
    ord_letters = []
    text = get_text()
    for char in text:
        ord_letters.append(str(ord(char)))

    return ord_letters


result = convert_to_ord()
print(','.join(result))

# -------------------------------------------
# chr()
# Unicode to text


def convert_unicode_to_alpha(unicodes):
    words = []
    for nums in unicodes:
        words.append(chr(int(nums)))

    return (words)


print(''.join(convert_unicode_to_alpha(result)))

# Example
# Enter the text : Hi my name is amir
# Letters to unicodes --> 72,105,32,109,121,32,110,97,109,101,32,105,115,32,97,109,105,114
# unicods to leeters -- > Hi my name is amir
