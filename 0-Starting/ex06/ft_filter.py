# list comprehension : parcourir une liste  en renvoyant une seconde  liste
#  modifiee ou filtree
# [valueur_de_retour for i in list_origine]

def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function:
        return ([item for item in iterable if function(item)])
    return ([item for item in iterable])


if __name__ == "__main__":

    original = filter.__doc__
    copy = ft_filter.__doc__
    print(copy)  # output: docstring
    print(original == copy)  # output: True
    print()

    def check_even(number):
        if number % 2 == 0:
            return True
        return False

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    strings = ["apple", "banana", "cherry", "date", "elderberry"]

    print("function None:")
    even_numbers_iterator = ft_filter(None, numbers)
    even_numbers = list(even_numbers_iterator)
    print("ft_filter:", even_numbers)

    even_numbers_iterator = filter(None, numbers)
    even_numbers = list(even_numbers_iterator)
    print("filter:", even_numbers)

    print()
    print("filter: even")
    # if an element passed to check_even() returns True, select it
    even_numbers_iterator = ft_filter(check_even, numbers)
    # converting to list
    even_numbers = list(even_numbers_iterator)
    print("ft_filter:", even_numbers)

    even_numbers_iterator = filter(check_even, numbers)
    even_numbers = list(even_numbers_iterator)
    print("filter:", even_numbers)

    print()
    print("fonction long string")
    long_strings_it = ft_filter(lambda s: len(s) > 5, strings)
    long_strings = list(long_strings_it)
    print("ft_filter:", long_strings)
    long_strings_it = filter(lambda s: len(s) > 5, strings)
    long_strings = list(long_strings_it)
    print("filter:", long_strings)
