from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''A Diamond class, for a "false" King'''

    def __init__(self, first_name, is_alive=True):
        '''Initializes a king character'''
        super().__init__(first_name, is_alive)

    def get_eyes(self):
		''' get eyes value'''
        return self.eyes

    def get_hairs(self):
		'''get hairs value'''
        return self.hairs

    def set_eyes(self, color):
		'''set eyes value'''
        try:
            if not isinstance(color, str):
                raise ValueError("enter a str")
        except ValueError as e:
            print(e)
        self.eyes = color

    def set_hairs(self, color):
		'''set hairs value'''
        try:
            if not isinstance(color, str):
                raise ValueError("enter a str")
        except ValueError as e:
            print(e)
        self.hairs = color


if __name__ == "__main__":
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")

    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)

    # error
    # Joffrey.set_eyes(123)
