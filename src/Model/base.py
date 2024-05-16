from abc import abstractmethod


class Base:
    @abstractmethod
    def insert_data(self):
        raise NotImplementedError("Define abstractmethod 'insert_data'")

    @abstractmethod
    def delete_data(self, id_delete):
        raise NotImplementedError("Define abstractmethod 'delete_data'")

    @abstractmethod
    def update_data(self):
        raise NotImplementedError("Define abstractmethod 'update_data'")

    @abstractmethod
    def search_data(self, search_id):
        raise NotImplementedError("Define abstractmethod 'search_info'")

