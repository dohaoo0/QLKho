from src.Model.Base import Base


class Actor(Base):
    def __init(self, id, name, email, phone, address, contract):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.contract = contract

