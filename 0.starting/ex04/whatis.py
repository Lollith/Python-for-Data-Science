# """Script that takes a number as argument, checks whether it is odd or even,
# and prints the result."""

import sys

if len(sys.argv) < 2:
    sys.exit(1)

try:
    try:	
        if len(sys.argv) > 2:
            raise AssertionError(": more than one argument is provided")

        int(sys.argv[1])  # si pas un int va return une erreur

    except ValueError:  # si pas un int
        raise AssertionError("argument is not an integer")

except AssertionError as error:
    print(AssertionError.__name__, error)
    sys.exit(1)

num = int(sys.argv[1])
if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
