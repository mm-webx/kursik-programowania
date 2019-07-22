from utils.models import BaseModel


class Account(BaseModel):
    name = None  # None | String
    birth_date = None  # None | Date
    email = None  # None | String
    password = None  # None | String
    phone_number = None  # None | String

    @classmethod
    def create(cls, name):
        acc = Account()
        acc.name = name

        return acc

    @property
    def name_in_ru(self):
        return (self.name)


class Driver(Account):
    has_driver_license = False  # Boolean
    actual_car = None  # None | Integer
    salary = 0.0  # Float


class Client(Account):
    discount = 0  # Integer


class Car(BaseModel):
    owner = None  # None | Integer
    model = None  # None | String
    color = None  # None | Color
    is_hybrid = False  # Boolean
