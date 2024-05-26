from src.Model.connect_db import ConnectDB


class Login:
    def __int__(self, input_id=None, input_password=None):
        self.input_id = input_id
        self.input_password = input_password

    @staticmethod
    def check_login(input_id=None, input_password=None):
        con = ConnectDB()
        con.connect()

        data_user = con.execute_query("""SELECT * FROM User;""")

        for data in data_user:
            if int(input_id) == data[0] and input_password == data[2]:
                if data[3] == "Quản lý":
                    return "Quản lý"
                return True
        return False
