import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """function that takes as parameters a 2D array, prints its shape, and
    returns a truncated version of the array based on the provided start and
    end arguments."""
    try:
        if not isinstance(family, list):
            raise TypeError("not a list")
    except TypeError as error:
        print(TypeError.__name__, ":", error)
    else:
        try:
            arr = np.array(family)
        except ValueError as error:
            print(ValueError.__name__, ":", error)
        else:
            print(f"My shape is: {arr.shape}")
            new_list = family[start:end]
            print(f"My new shape is: {np.array(new_list).shape}")
            return new_list


if __name__ == "__main__":
    family = [[1.80, 78.4], 
              [2.15, 102.7], 
              [2.10, 98.5], 
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print()

    print("Not a list: ")
    family = "coucou"
    print(slice_me(family, 0, 2))
    print()

    print("size error:")
    family = [[1.80], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
