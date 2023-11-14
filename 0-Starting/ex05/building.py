""" Autonomous program, witch takes a single string arg and displays the sums
of its upper-case characters, lower-case characters, punctuation characters,
digits and spaces """


import sys


def main():
    my_str_ponct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    char_dict = {
        "upper letters": 0,
        "lower letters": 0,
        "punctuation marks": 0,
        "spaces": 0,
        "digits": 0,
    }
    try:
        if len(sys.argv) > 2:
            raise AssertionError(": more than one argument is provided")
    except AssertionError as error:
        print(AssertionError.__name__, error, sep="")
        sys.exit(1)

    if len(sys.argv) != 2:
        sentence = input("What is the text to count?\n")
    else:
        sentence = sys.argv[1]
    print(f"The text contains {len(sentence)} characters:")
    for letter in sentence:
        if letter.isupper():
            char_dict["upper letters"] += 1
        if letter.islower():
            char_dict["lower letters"] += 1
        for punct in my_str_ponct:
            if letter == punct:
                char_dict["punctuation marks"] += 1
        if letter == " ":
            char_dict["spaces"] += 1
        if letter.isdigit():
            char_dict["digits"] += 1
    for cle, valeur in char_dict.items():
        print(valeur, cle)


if __name__ == "__main__":
    main()
