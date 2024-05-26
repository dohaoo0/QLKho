from src.Model.base import Base


class User(Base):
    def __init__(self, id=None, name=None, password=None, role=None):
        self.id = id
        self.name = name
        self.password = password
        self. role = role

    def insert_data(self):
        insert_query = f"INSERT INTO User (IdUser, NameUser, Password, Role) VALUES \
                       ('{self.id}', '{self.name}', '{self.password}', '{self.role}');"
        return insert_query

    def delete_data(self, id_delete):
        delete_query = f"DELETE FROM User WHERE IdUser = '{id_delete}'"
        return delete_query

    def update_data(self):
        update_query = f"UPDATE User SET IdUser = '{self.id}', NameUser = '{self.name}',\
                        Password = '{self.password}, Role = '{self.role}'"
        return update_query

    def search_data(self, search_id):
        where = ';'
        if search_id != '':
            where = f"WHERE IdUser = '{search_id}';"
        search_query = f"SELECT * FROM User " + where
        return search_query
