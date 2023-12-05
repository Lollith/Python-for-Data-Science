from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''A Diamond class, for a "false" King'''

    def __init__(self, first_name, is_alive=True):
        '''Initializes a king character'''
        Baratheon.__init__(self, first_name, is_alive)

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, color):
        if not isinstance(color, str):
            raise ValueError("need str")
        self.eyes = color


if __name__ == "__main__":
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    # Joffrey.set_eyes("blue")
    Joffrey.set_eyes(123)

    # Joffrey.set_hairs("light")
    # print(Joffrey.get_eyes())
    # print(Joffrey.get_hairs())
    # print(Joffrey.__dict__)