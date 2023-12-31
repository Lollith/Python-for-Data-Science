# global is forbidden
# une fonction est un objet.

def square(x: int | float) -> int | float:
    '''Returns the square of argument.'''
    return (x ** 2)


def pow(x: int | float) -> int | float:
    '''returns the Exponentiation of argument by himself.'''
    return (x ** x)


def outer(x: int | float, function) -> object:
    '''Takes as argument a number and a function, it returns an object that
    when called returns the result of the arguments calculation.'''
    count = 0

    def inner() -> float:
        nonlocal count
        nonlocal x  # permet de modifier x
        count = count + 1  # compte le nombre d'appel de ma fonction
        # print(f'{count} appels de {function.__name__}')
        x = function(x)
        return (x)

    return (inner)  # not called, create a "closure"


if __name__ == "__main__":
    my_counter = outer(3, square)
    print(my_counter())  # called here
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())
