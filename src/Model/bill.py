from src.Model.base import Base


class Bill(Base):
    def __init__(self, id=None, idactor=None, iduser=None, products=None, price=None, quantity=None, date=None):
        self.id = id
        self.idactor = idactor
        self.iduser = iduser
        self.products = products
        self.price = price
        self.quantity = quantity
        self.date = date
