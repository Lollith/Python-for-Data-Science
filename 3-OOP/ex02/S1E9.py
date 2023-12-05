from abc import ABC, abstractmethod


class Character(ABC):
    '''A Abstract base class used to create a character,
        2 parameters'''

    def __init__(self, first_name: str, is_alive: bool = True):
        '''Initializes a character with 2 arguments,first_name and \
is_alive.'''
        self._first_name = first_name
        self._is_alive = is_alive

    @abstractmethod
    def die(self):
        '''Changes health state of the caracter.'''
        pass


class Stark(Character):
    '''An inherited class of Character, create a Stark.'''

    def __init__(self, first_name: str, is_alive: bool = True):
        '''Initializes a Stark character with 2 arguments, first_name and \
is_alive.'''
        Character.__init__(self, first_name, is_alive)

    def die(self):
        '''Changes health state of the caracter.'''
        self._is_alive = False


if __name__ == "__main__":
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned._is_alive)  # must be protected, use setter/getter
    Ned.die()
    print(Ned._is_alive)
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
