"""program that accepts two arguments: a string(S), and an integer(N).
The program should output a list of words from S that have a length greater
than N."""

#  f = lambda arg1, arg2 : instruction de retour
# all(...):retourne True si toutes les conditions dans la liste sont vraies
# pour chaque caractère de la chaîne.

import sys
from ft_filter import ft_filter


def main():
    try:
        try:
            if len(sys.argv) != 3:
                raise AssertionError("the arguments are bad")
            n = int(sys.argv[2])
            is_valid = all((c.isalpha() or c.isspace()) and c.isprintable()
                           for c in sys.argv[1])
            if not is_valid:
                raise AssertionError("the argument are bad: not alpha")
        except ValueError:
            raise AssertionError("the argument are bad: wrong type")
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    else:
        list_arg = sys.argv[1].split()
        list_arg_n = list(ft_filter((lambda arg: len(arg) > n), list_arg))
        print(list_arg_n)


if __name__ == "__main__":
    main()
