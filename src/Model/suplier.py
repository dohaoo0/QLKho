from src.Model.actor import Actor


class Suplier(Actor):
    def __init__(self, id=None, name=None, email=None, phone=None, address=None, contract=None):
        super(Suplier, self).__init__(id, name, email, phone, address, contract)

    def insert_data(self):
        insert_query = f"\
            INSERT INTO Suplier (IdSuplier, NameSuplier, Email, Phone, Address, Contract) \
            VALUES ('{self.id}', '{self.name}', '{self.email}', '{self.phone}', '{self.address}', '{self.contract}')"
        return insert_query

    def delete_data(self, id_delete):
        delete_query = f"DELETE FROM Suplier WHERE IdSuplier = '{id_delete}'"
        return delete_query

    def update_data(self):
        update_query = f"UPDATE Suplier SET \
                        IdSuplier = '{self.id}', NameSuplier = '{self.name}', Email = '{self.email}',\
                        Phone ='{self.phone}', Address = '{self.address}', Contract = '{self.contract}'"
        return update_query

    def search_data(self, search_id=''):
        where = ';'
        if search_id != '':
            where = f"WHERE IdSuplier = '{search_id}';"
        search_query = f"SELECT * FROM Suplier " + where
        return search_query
