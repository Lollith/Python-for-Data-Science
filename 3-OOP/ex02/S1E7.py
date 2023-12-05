from S1E9 import Character


class Baratheon(Character):
    '''An inherited class of Character, create a Baratheon.'''

    def __init__(self, first_name: str, is_alive: bool = True):
        '''Initializes a character with 2 arguments,first_name and \
            is_alive, allow to instantiate without going through the Character\
                class.'''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        '''Method which change health state of the caracter.'''
        self._is_alive = False

    def __str__(self):
        '''Override the __str__ methods, return sting instead of objects'''
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        '''Override the _repr__ methods, return sting instead of objects'''
        # return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
        return self.__str__()


class Lannister(Character):
    '''An inherited class of Character, create a Lannister.'''

    def __init__(self, first_name, is_alive=True):
        '''Initializes a charracter with 2 arguments,first_name and \
            is_alive, allow to instantiate without going through the Character\
                class.'''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        '''Method which change health state of the caracter.'''
        self._is_alive = False

    def __str__(self):
        """Override the __str__ methods, return sting instead of objects"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Override the _repr__ methods, return sting instead of objects"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """ Create a chain of Lannister, return an instance"""
        member = cls(first_name, is_alive)
        return member


if __name__ == "__main__":
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert._is_alive)
    Robert.die()
    print(Robert._is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei._is_alive)
    print("---")

    # appel sur la class directement => classmethod :
    Jaine = Lannister.create_lannister("Jaine", True)
    # rappel , rajouter _ par raport au sujet car devrait etre protected:
    print(f"Name : {Jaine._first_name, type(Jaine).__name__},\
Alive : {Jaine._is_alive}")
