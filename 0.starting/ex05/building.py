""" Autonomous program, witch takes a single string arg and displays the sums 
of its upper-case characters, lower-case characters, punctuation characters, 
digits and spaces """

# use exception
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
        if len(sys.argv) != 2:
            raise AssertionError("What is the text to count?")
    except AssertionError as error:
        print(error)
        sentence = "Hello World! "
        print(sentence)
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
