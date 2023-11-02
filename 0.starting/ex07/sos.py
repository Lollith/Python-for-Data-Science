"""Program thar takes a string as an argument and encode it into Morse Code"""

import sys


def main():
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    morce_list = []
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")   
        is_valid = all((c.isalnum() or c.isspace()) and c.isprintable()
                       for c in sys.argv[1])
        if not is_valid:
            raise AssertionError("the argument are bad: not alphanumeric")
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    else:
        sentence = sys.argv[1].upper()
        for c in sentence:
            if c in NESTED_MORSE:
                morce_list.append(NESTED_MORSE[c])
                morce = " ".join(morce_list)
        print(morce)


if __name__ == "__main__":
    main()
