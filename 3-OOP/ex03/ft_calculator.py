class calculator:
    ''' calculator class ables to do calculations: addition, multiplication,\
        substraction and division of vector with a scalar'''

    def __init__(self):
        ''' Initializes the calculator'''
    def __add__(self, object) -> None:
        ''' '''
    def __mul__(self, object) -> None:
        ''' '''
    def __sub__(self, object) -> None:
        ''' '''
    def __truediv__(self, object) -> None:
        ''' '''


if __name__ == "__main__":
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
