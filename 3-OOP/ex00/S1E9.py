from abc import ABC, abstractmethod


class Character(ABC):
    '''A Class used to create a character, 2 protected parameters'''
    def __init__(self, first_name, is_alive=True):
        '''Initiate the object. 2 arguments, first_name and is_alive.'''
        self.__first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        '''Method which change health state of the caracter.'''
        pass


class Stark(Character):
    '''An inherited class of Character, create a Stark.'''
    def __init__(self, first_name, is_alive=True):
        '''Initiate the object. 2 arguments, first_name and is_alive.'''
        self.__first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''Method which change health state of the caracter.'''
        self.is_alive = False


if __name__ == "__main__":
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    try:
        hodor = Character("hodor")
    except TypeError as e:
        print(TypeError.__name__, e, sep=": ")
