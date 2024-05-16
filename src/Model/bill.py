from src.Model.base import Base


class Bill(Base):
    def __init__(self, id, idactor, iduser, products, quantity, date):
        self.id = id
        self.idactor = idactor
        self.iduser = iduser
        self.products = products
        self.quantity = quantity
        self.date = date
