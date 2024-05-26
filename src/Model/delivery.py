from src.Model.bill import Bill


class Delivery(Bill):
    def __init__(self, id=None, idactor=None, iduser=None, products=None, price=None, quantity=None, date=None):
        super(Delivery, self).__init__(id, idactor, iduser, products, price, quantity, date)

    def insert_data(self):
        insert_detail = f"INSERT INTO deli_detail (IdDelivery,IdProduct,Price,Quantity) \
                    VALUES ('{self.id}', '{self.products}', '{self.price}', '{self.quantity}')"
        insert_query = f"\
            INSERT INTO Delivery (IdDelivery, IdCustomer, IdUser, Date) \
            VALUES ('{self.id}', '{self.idactor}', '{self.iduser}', '{self.date}')"
        return insert_query, insert_detail

    def delete_data(self, id_delete):
        delete_detail = f"DELETE FROM deli_detail WHERE IdDelivery = '{id_delete}';"
        delete_query = f"DELETE FROM Delivery WHERE IdDelivery = '{id_delete}';"
        return delete_detail, delete_query

    def update_data(self):
        update_query = f"UPDATE Delivery SET\
            IdDelivery = '{self.id}', IdCustomer = '{self.idactor}', IdUser = '{self.iduser}',\
            Date = '{self.date}'"
        return update_query

    def search_data(self, search_id=''):
        where = ';'
        if search_id != '':
            where = f"WHERE IdDelivery = '{self.id}';"
        search_query = "SELECT * FROM Delivery " + where
        return search_query
