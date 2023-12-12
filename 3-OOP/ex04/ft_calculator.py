class Calculator:
    '''Calculator class ables to do dotproduct, addition, substraction of 2\
        vectors '''

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        '''dotproduct of 2 vectors'''
        try:
            if (len(V1) == len(V2)):
                print(sum([i * j for i, j in zip(V1, V2)]))
            else:
                raise AssertionError("Not same size")
        except AssertionError as e:
            print(AssertionError.__name__, e, sep=": ")

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        '''addition of 2 vectors'''
        try:
            if (len(V1) == len(V2)):
                print([float(i + j) for i, j in zip(V1, V2)])
            else:
                raise AssertionError("Not same size")
        except AssertionError as e:
            print(AssertionError.__name__, e, sep=": ")

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        '''substraction of 2 vectors'''
        try:
            if (len(V1) == len(V2)):
                print([float(i - j) for i, j in zip(V1, V2)])
            else:
                raise AssertionError("Not same size")
        except AssertionError as e:
            print(AssertionError.__name__, e, sep=": ")


if __name__ == "__main__":
    a = [5, 10, 2]
    b = [2, 4, 3]
    Calculator.dotproduct(a, b)
    Calculator.add_vec(a, b)
    Calculator.sous_vec(a, b)
