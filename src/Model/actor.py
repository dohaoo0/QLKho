from src.Model.base import Base


class Actor(Base):
    def __init__(self, id=None, name=None, email=None, phone=None, address=None, contract=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.contract = contract
