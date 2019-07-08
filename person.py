class Person(object):
    name = None
    age = 0
    is_single = True

    def __init__(self, name, age=6, is_single=True):
        self.name = name
        self.age = age
        self.is_single = is_single

    def is_mature(self):
        if self.age >= 18:
            return True
        else:
            return False
