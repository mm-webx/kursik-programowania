from utils.models import BaseModel


class Order(BaseModel):
    driver = ""
    client = ""
    address_from = ""
    address_to = ""
    date = "1990-01-01 00:00"
