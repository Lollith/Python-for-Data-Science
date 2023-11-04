def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Take 2 lists of intergers or floats in input and returns a list of BMI
    values."""
    try:
        if (len(height) != len(weight)):
            raise AssertionError("Not same Size")
    except AssertionError as error:
        print(AssertionError.__name__,":", error)
    else:
        return [w / h ** 2 for w, h in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Accepts a list of integers or floats and an integer representing a limit
    as parameters"""
    try:
        return [b >= limit for b in bmi]
    except TypeError:
        print("Error: list does'nt exist")


if __name__ == "__main__":
    print("subject 42: ")
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    print()
    print("Not same size: ")
    height = [2.71, 1.15, 2.1]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    print()
    print("Not int/float")