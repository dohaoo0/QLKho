from src.Model.bill import Bill


class Delivery(Bill):
    def insert_data(self):
        insert_query = f"\
            INSERT INTO Delivery (IdDelivery, IdCustomer, IdUser, Products, Quantity, Date) \
            VALUES '{self.id}', '{self.idactor}', '{self.iduser}', '{self.products}', '{self.quantity}', '{self.date}'"
        return insert_query

    def delete_data(self, id_delete):
        delete_query = f"DELETE FROM Delivery WHERE IdDelivery = '{id_delete}'"
        return delete_query

    def update_data(self):
        update_query = f"UPDATE Delivery SET\
            IdDelivery = '{self.id}', IdCustomer = '{self.idactor}', IdUser = '{self.iduser}',\
            Products = '{self.products}', Quantity = '{self.quantity}', Date = '{self.date}'"
        return update_query

    def search_data(self, search_id=''):
        where = ';'
        if search_id != '':
            where = f"WHERE IdDelivery = '{self.id}'"
        search_query = "SELECT * FROM Delivery" + where
        return search_query
