from src.Model.actor import Actor


class Customer(Actor):
    def insert_data(self):
        insert_query = f"\
            INSERT INTO Customer (IdCustomer, NameCustomer, Email, Phone, Address, ContractDate) \
            VALUES ('{self.id}', '{self.name}', '{self.email}', '{self.phone}', '{self.address}', '{self.contract}')"
        return insert_query

    def delete_data(self, id_delete):
        delete_query = f"DELETE FROM Customer WHERE IdCustomer = '{id_delete}'"
        return delete_query

    def update_data(self):
        update_query = f"UPDATE Customer SET \
                        IdCustomer = '{self.id}', NameCustomer = '{self.name}', Email = '{self.email}',\
                        Phone ='{self.phone}', Address = '{self.address}', ContractDate = '{self.contract}'"
        return update_query

    def search_data(self, search_id=''):
        where = ';'
        if search_id != '':
            where = f"WHERE IdCustomer = '{search_id}';"
        search_query = f"SELECT * FROM Customer " + where
        return search_query
