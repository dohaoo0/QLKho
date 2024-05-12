from src.Model.ConnectDb import ConnectDB


class User:
    def __int__(self, input_id, input_password):
        self.input_id = input_id
        self.input_password = input_password

    def check_login(self):
        con = ConnectDB()
        con.connect()

        data_user = con.execute_query("""SELECT * FROM User;""")

        for data in data_user:
            if self.input_id == data[0] and self.input_password == data[1]:
                return True
        return False

    
