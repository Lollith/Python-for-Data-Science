import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass()
class Student:
    '''Dataclass tha takes as arguments a name and a nickname, set active to
    True, create the student login, and generate a random ID with generate_id
    function.'''
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname


if __name__ == "__main__":
    student = Student(name="Edward", surname="agle")
    print(student)
    print()

    try:
        student = Student(name="Edward", surname="agle", login="toto")
        print(student)
    except TypeError as e:
        print(TypeError.__name__, e, sep=": ")
        print()

    try:
        student = Student(name="Edward", surname="agle", id="toto")
        print(student)
    except TypeError as e:
        print(TypeError.__name__, e, sep=": ")
