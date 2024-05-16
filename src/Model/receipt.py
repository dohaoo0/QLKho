from src.Model.bill import Bill


class Receipt(Bill):
    def insert_data(self):
        insert_query = f"\
            INSERT INTO Receipt (IdReceipt, IdSuplier, IdUser, Products, Quantity, Date) \
            VALUES '{self.id}', '{self.idactor}', '{self.iduser}', '{self.products}', '{self.quantity}', '{self.date}'"
        return insert_query

    def delete_data(self, id_delete):
        delete_query = f"DELETE FROM Receipt WHERE IdReceipt = '{id_delete}'"
        return delete_query

    def update_data(self):
        update_query = f"UPDATE Receipt SET\
            IdReceipt = '{self.id}', IdSUplier = '{self.idactor}', IdUser = '{self.iduser}',\
            Products = '{self.products}', Quantity = '{self.quantity}', Date = '{self.date}'"
        return update_query

    def search_data(self, search_id=''):
        where = ';'
        if search_id != '':
            where = f"WHERE IdReceipt = '{self.id}'"
        search_query = "SELECT * FROM Receipt" + where
        return search_query
