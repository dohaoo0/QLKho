import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import uic

from src.Model.connectDb import ConnectDB
from src.Model.product import Product
from src.Model.receipt import Receipt
from src.Model.delivery import Delivery
from src.Model.suplier import Suplier
from src.Model.customer import Customer
from src.Model.tablemodel import TableModel


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = uic.loadUi(r"..\View\manage.ui", self)
        self.conn = ConnectDB()
        self.model = None

        #Lay thong tin tu giao dien Hang hoa
        self.pro_input_search = self.findChild(QtWidgets.QLineEdit, "pro_input_search")
        self.pro_button_search = self.findChild(QtWidgets.QPushButton, "pro_button_search")
        self.pro_button_search.clicked.connect(lambda: self.on_pro_button_search_clicked)
        self.pro_button_add = self.findChild(QtWidgets.QPushButton, "pro_button_add")
        self.pro_button_add.clicked.connect(lambda: self.on_pro_button_add_clicked)
        self.pro_table_view = self.findChild(QtWidgets.QTableWidget, "pro_table_view")

        #Lay thong tin tu giao dien Nhap kho
        self.rec_input_search = self.findChild(QtWidgets.QLineEdit, "rec_input_search")
        self.rec_button_seach = self.findChild(QtWidgets.QPushButton, "rec_button_seach")
        self.rec_button_seach.clicked.connect(self.on_rec_button_search_clicked)
        self.rec_button_add = self.findChild(QtWidgets.QPushButton, "rec_button_add")
        self.rec_button_add.clicked.connect(self.on_rec_button_add_clicked)
        self.rec_table_vew = self.findChild(QtWidgets.QTabWidget, "rec_table_vew")

        # Lay thong tin tu giao dien Xuat kho
        self.deli_input_search = self.findChild(QtWidgets.QLineEdit, "deli_input_search")
        self.deli_button_search = self.findChild(QtWidgets.QPushButton, "deli_button_search")
        self.deli_button_search.clicked.connect(self.on_deli_button_search_clicked)
        self.deli_button_add = self.findChild(QtWidgets.QPushButton, "deli_button_add")
        self.deli_button_add.clicked.connect(self.on_deli_button_add_clicked)
        self.deli_table_view = self.findChild(QtWidgets.QTabWidget, "deli_table_view")

        # Lay thong tin tu giao dien Nha cung cap
        self.sup_input_search = self.findChild(QtWidgets.QLineEdit, "sup_input_search")
        self.sup_button_search = self.findChild(QtWidgets.QPushButton, "sup_button_search")
        self.sup_button_search.clicked.connect(self.on_sup_button_search_clicked)
        self.sup_button_add = self.findChild(QtWidgets.QPushButton, "sup_button_add")
        self.sup_button_add.clicked.connect(self.on_sup_button_add_clicked)
        self.sup_table_view = self.findChild(QtWidgets.QTabWidget, "sup_table_view")

        #Lay thong tin tu giao dien Khach hang
        self.cus_input_search = self.findChild(QtWidgets.QLineEdit, "cus_input_search")
        self.cus_button_search = self.findChild(QtWidgets.QPushButton, "sup_button_search")
        self.cus_button_search.clicked.connect(self.on_cus_button_search_clicked)
        self.cus_button_add = self.findChild(QtWidgets.QPushButton, "cus_button_add")
        self.cus_button_add.clicked.connect(self.on_cus_button_add_clicked)
        self.cus_table_view = self.findChild(QtWidgets.QTabWidget, "cus_table_view")

        #lay thong tin tu bang Tai khoan
        self.user_input_search = self.findChild(QtWidgets.QLineEdit, "user_input_search")
        self.user_button_search = self.findChild(QtWidgets.QPushButton, "user_button_search")
        self.user_button_search.clicked.connect(self.on_user_button_search_clicked)
        self.user_button_add = self.findChild(QtWidgets.QPushButton, "user_button_add")
        self.user_button_add.clicked.connect(self.on_user_button_add_clicked)
        self.user_table_view = self.findChild(QtWidgets.QTabWidget, "user_table_view")

    def on_pro_button_search_clicked(self):
        pass

    def get_data_search(self):
        pro_search_id = self.pro_input_search.text().strip()
        pro = Product(pro_search_id)
        return pro

    def on_pro_button_add_clicked(self):
        pro = self.get_data_search()
        search_query = pro.search_data(pro.id)
        pro_table = self.conn.execute_query(search_query)

        if len(pro_table) > 0:
            self.model = None
            header = ['Mã sản phẩm', 'Tên sản phẩm', 'Chiều dài', 'Chiều rộng', 'Chiều cao']
            self.model = TableModel(pro_table, header)

            self.pro_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.pro_table_view.horizontalHeader().setStretchLastSection(True)
            self.pro_table_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)


    def on_rec_button_search_clicked(self):
        pass
    def on_rec_button_add_clicked(self):
        pass


    def on_deli_button_search_clicked(self):
        pass
    def on_deli_button_add_clicked(self):
        pass


    def on_sup_button_search_clicked(self):
        pass
    def on_sup_button_add_clicked(self):
        pass


    def on_cus_button_search_clicked(self):
        pass
    def on_cus_button_add_clicked(self):
        pass



    def on_user_button_search_clicked(self):
        pass
    def on_user_button_add_clicked(self):
        pass

    @staticmethod
    def show_log(title, log):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setInformativeText(log)
        msg.setIcon(QMessageBox.Icon.Information)

        # Hiển thị hộp thông báo
        msg.exec()

    def closeEvent(self, event):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText("<font color = red >Bạn có muốn thoát ứng dụng? </font >")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg_box.setStyleSheet("background-color: rgb(241, 241, 241);")
        ret = msg_box.exec()
        if ret == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()