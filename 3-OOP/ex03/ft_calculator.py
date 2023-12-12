class calculator:
    ''' calculator class ables to do calculations: addition, multiplication,
        substraction and division of vector with a scalar'''

    def __init__(self, my_object):
        '''Initializes the calculator.'''
        self.my_object = my_object

    def __add__(self, object_right) -> None:
        '''Addition of 2 objects and print a new object.'''
        self.my_object = ([i + object_right for i in self.my_object])
        print(self.my_object)

    def __mul__(self, object_right) -> None:
        '''multiplication of 2 objects and print a new object'''
        self.my_object = [i * object_right for i in self.my_object]
        print(self.my_object)

    def __sub__(self, object_right) -> None:
        '''substraction of 2 objects and print a new object'''
        self.my_object = [i - object_right for i in self.my_object]
        print(self.my_object)

    def __truediv__(self, object_right) -> None:
        '''division of 2 objects ans print a new object'''
        try:
            self.my_object = [i / object_right for i in self.my_object]
        except ZeroDivisionError as e:
            print(ZeroDivisionError.__name__, e, sep=": ")
        else:
            print(self.my_object)


if __name__ == "__main__":
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5  # manip de l'instance
    v3 / 0
