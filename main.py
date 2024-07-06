from random import shuffle, uniform
from time import sleep


def sanitize_input(text):
    text.lower()
    characters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '?'
    ]
    rady = ""
    for letter in text:
        sleep(uniform(0.100, 0.160))
        shuffle(characters)
        for character in characters:
            print(f"{rady}{character}")
            if letter == character:
                rady += character
                break


if __name__ == '__main__':
    word = input("Write word: ").lower()
    sanitize_input(word)

