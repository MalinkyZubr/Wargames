import string


possibilities = ['g', 'd', '7', '2', '3', 'l', 'b', 'y', '9', '8', '0', 'a', '4', 'u', 'n', 'j', '1', 'k', 'c', 'e', 'i', 'q', '5', 't', 'r']


def iterate_strings(string, length):
    print(string)
    if len(string) - 1 < length:
        for character in possibilities:
            iterate_strings(string + character, length)


iterate_strings("", 10)
    