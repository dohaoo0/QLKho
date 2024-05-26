import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QMenu
from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6 import uic

from src.Model.connect_db import ConnectDB
from src.Model.product import Product
from src.Model.receipt import Receipt
from src.Model.delivery import Delivery
from src.Model.suplier import Suplier
from src.Model.customer import Customer
from src.Model.user import User


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = uic.loadUi(r"View\manage.ui", self)
        self.conn = ConnectDB()
        self.conn.connect()

        # Lay thong tin tu giao dien Hang hoa
        self.pro_input_search = self.ui.pro_input_search
        self.pro_button_search = self.ui.pro_button_search
        self.pro_button_search.clicked.connect(lambda: self.on_pro_button_search_clicked)
        self.pro_button_add = self.ui.pro_button_add
        self.pro_button_add.clicked.connect(lambda: self.on_pro_button_add_clicked)
        self.pro_table_view = self.ui.pro_table_view
        self.pro_table_view.setSortingEnabled(False)
        self.pro_show_data()

        # Lay thong tin tu giao dien Nhap kho
        self.rec_input_search = self.ui.rec_input_search
        self.rec_button_search = self.ui.rec_button_search
        self.rec_button_search.clicked.connect(lambda: self.on_rec_button_search_clicked)
        self.rec_button_add = self.ui.rec_button_add
        self.rec_button_add.clicked.connect(lambda: self.on_rec_button_add_clicked)
        self.rec_table_view = self.ui.rec_table_view
        self.rec_table_view.setSortingEnabled(False)
        self.rec_show_data()

        # Lay thong tin tu giao dien Xuat kho
        self.deli_input_search = self.ui.deli_input_search
        self.deli_button_search = self.ui.deli_button_search
        self.deli_button_search.clicked.connect(lambda: self.on_deli_button_search_clicked)
        self.deli_button_add = self.ui.deli_button_add
        self.deli_button_add.clicked.connect(lambda: self.on_deli_button_add_clicked)
        self.deli_table_view = self.ui.deli_table_view
        self.deli_table_view.setSortingEnabled(False)
        self.deli_show_data()

        # Lay thong tin tu giao dien Nha cung cap
        self.sup_input_search = self.ui.sup_input_search
        self.sup_button_search = self.ui.sup_button_search
        self.sup_button_search.clicked.connect(lambda: self.on_sup_button_search_clicked)
        self.sup_button_add = self.ui.sup_button_add
        self.sup_button_add.clicked.connect(lambda: self.on_sup_button_add_clicked)
        self.sup_table_view = self.ui.sup_table_view
        self.sup_table_view.setSortingEnabled(False)
        self.sup_show_data()

        # Lay thong tin tu giao dien Khach hang
        self.cus_input_search = self.ui.cus_input_search
        self.cus_button_search = self.ui.sup_button_search
        self.cus_button_search.clicked.connect(lambda: self.on_cus_button_search_clicked)
        self.cus_button_add = self.ui.cus_button_add
        self.cus_button_add.clicked.connect(lambda: self.on_cus_button_add_clicked)
        self.cus_table_view = self.ui.cus_table_view
        self.cus_table_view.setSortingEnabled(False)
        self.cus_show_data()

        # lay thong tin tu bang Tai khoan
        self.user_input_search = self.ui.user_input_search
        self.user_button_search = self.ui.user_button_search
        self.user_button_search.clicked.connect(lambda: self.on_user_button_search_clicked)
        self.user_button_add = self.ui.user_button_add
        self.user_button_add.clicked.connect(lambda: self.on_user_button_add_clicked)
        self.user_table_view = self.ui.user_table_view
        self.user_table_view.setSortingEnabled(False)
        self.user_show_data()

        # Lay thong tin cac tab
        self.tab = self.ui.tab
        self.create_menu(self.pro_table_view)
        self.create_menu(self.deli_table_view)
        self.create_menu(self.sup_table_view)
        self.create_menu(self.cus_table_view)
        self.create_menu(self.rec_table_view)
        self.create_menu(self.user_table_view)

    def create_menu(self, table_view):
        table_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        table_view.customContextMenuRequested.connect(lambda pos: self.show_context_menu(pos, table_view))

    def show_context_menu(self, pos, table_view):
        # Lấy vị trí con trỏ chuột
        row = table_view.rowAt(pos.y())

        # Tạo menu ngữ cảnh
        menu = QMenu()

        # Thêm tùy chọn xóa
        delete_action = menu.addAction("Xóa")

        # Thêm tùy chọn lưu
        save_action = menu.addAction("Lưu")

        delete_action.triggered.connect(lambda: self.delete_item(row, table_view))
        save_action.triggered.connect(lambda: self.save_data(table_view))

        # Hiển thị menu ngữ cảnh
        menu.exec(table_view.mapToGlobal(pos))

    @staticmethod
    def check_name_table(table_view):
        table_name = table_view.objectName()
        selected_items = table_view.selectedItems()
        object = None
        if table_name == 'pro_table_view':
            object = Product(selected_items[0].text(), selected_items[1].text(), selected_items[2].text(),
                             selected_items[3].text(),
                             selected_items[4].text())
        elif table_name == 'rec_table_view':
            object = Receipt(selected_items[0].text(), selected_items[1].text(), selected_items[2].text(),
                             selected_items[3].text(),
                             selected_items[4].text(), selected_items[5].text())
        elif table_name == 'deli_table_view':
            object = Delivery(selected_items[0].text(), selected_items[1].text(), selected_items[2].text(),
                              selected_items[3].text(),
                              selected_items[4].text(), selected_items[5].text())
        elif table_name == 'sup_table_view':
            object = Suplier(selected_items[0].text(), selected_items[1].text(), selected_items[2].text(),
                             selected_items[3].text(),
                             selected_items[4].text(), selected_items[5].text())
        elif table_name == 'cus_table_view':
            object = Customer(selected_items[0].text(), selected_items[1].text(), selected_items[2].text(),
                              selected_items[3].text(),
                              selected_items[4].text(), selected_items[5].text())
        elif table_name == 'user_table_view':
            object = User(selected_items[0].text(), selected_items[1].text(), selected_items[2].text(),
                          selected_items[3].text())
        return object

    def delete_item(self, row, table_view):
        result = QMessageBox.question(self, "Xác nhận xóa", "Bạn có chắc chắn muốn xóa?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.No)

        # Kiểm tra kết quả
        if result == QMessageBox.StandardButton.Yes:
            # Xóa mục được chọn
            object = self.check_name_table(table_view)
            delete_query = object.delete_data(object.id)
            if isinstance(delete_query, str):
                self.conn.execute_query(delete_query, fetch=False)
            else:
                self.conn.execute_query(delete_query[0], fetch=False)
                self.conn.execute_query(delete_query[1], fetch=False)
            table_view.removeRow(row)
            self.show_all_table()

        # pass

    def show_all_table(self):

        self.pro_show_data()
        self.sup_show_data()
        self.rec_show_data()
        self.deli_show_data()
        self.user_show_data()
        self.cus_show_data()

    def save_data(self, table_view):
        result = QMessageBox.question(self, "Xác nhận lưu", "Bạn có chắc chắn muốn lưu?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.No)
        if result == QMessageBox.StandardButton.Yes:
            object = self.check_name_table(table_view)
            insert_query = object.insert_data()
            if isinstance(insert_query, str):
                self.conn.execute_query(insert_query, fetch=False)
            else:
                selected_items = table_view.selectedItems()
                self.conn.execute_query(insert_query[0], fetch=False)
                self.conn.execute_query(insert_query[1], fetch=False)
                pro = Product()
                search_query = pro.search_data(selected_items[3].text())
                data = self.conn.execute_query(search_query)
                if len(data) > 0:
                    # Cập nhật số lượng tồn kho
                    if data[0][4] in ['None', None]:
                        inventory = 0
                    else:
                        inventory = int(data[0][4])
                    if 'deli' in insert_query[0].lower():
                        inventory = str(inventory - int(selected_items[5].text()))
                    else:
                        inventory = str(inventory + int(selected_items[5].text()))
                    pro_new = Product(data[0][0], data[0][1], data[0][2], data[0][3], inventory)
                    query = pro_new.update_data()
                    self.conn.execute_query(query, fetch=False)
                    title = "Thông báo"
                    log = "Đã thêm thành công"
                else:
                    title = "Thông báo"
                    log = " chưa có sản phầm trong kho"
                self.show_log(title, log)
        self.show_all_table()

    def show_data(self, table_data, table_view, header=None):
        if len(table_data) > 0:
            table_view.setRowCount(len(table_data))
            table_view.setColumnCount(len(table_data[0]))
            table_view.setHorizontalHeaderLabels(header)
            for c in range(0, len(table_data)):
                for r in range(0, len(table_data[0])):
                    s = str(table_data[c][r])
                    i = QTableWidgetItem(s)
                    table_view.setItem(c, r, i)
        else:
            title = "Thông báo"
            log = "Không có dữ liệu"
            self.show_log(title, log)

    @staticmethod
    def message_box():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText("<font color = red >Bạn có chắc chắn muốn xóa? </font >")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg_box.setStyleSheet("background-color: rgb(241, 241, 241);")
        ret = msg_box.exec()
        if ret == QtWidgets.QMessageBox.StandardButton.No:
            msg_box.close()
        return ret

    def pro_show_data(self):
        show_query = "SELECT * FROM Product;"
        data = self.conn.execute_query(show_query)
        header = ['Mã sản phẩm', 'Tên sản phẩm', 'Dài x Rộng x Cao', 'Khu vực chứa', 'Tồn kho']

        self.show_data(data, self.pro_table_view, header)

    @pyqtSlot()
    def on_pro_button_search_clicked(self):
        pro_search_id = self.pro_input_search.text().strip()
        product = Product()
        search_query = product.search_data(pro_search_id)
        pro_table = self.conn.execute_query(search_query)
        header = ['Mã sản phẩm', 'Tên sản phẩm', 'Dài x Rộng x Cao', 'Khu vực chứa', 'Tồn kho']
        self.show_data(pro_table, self.pro_table_view, header)

    @pyqtSlot()
    def on_pro_button_add_clicked(self):
        cur = self.pro_table_view.rowCount()
        self.pro_table_view.insertRow(cur)

    def rec_show_data(self):
        show_query = "select re.idreceipt, re.idsuplier, re.iduser, rd.idproduct, rd.price, rd.quantity, re.date\
                    from receipt as re join rec_detail as rd on re.idreceipt = rd.idreceipt\
                    order by re.idreceipt asc;"
        data = self.conn.execute_query(show_query)
        header = ["Mã phiếu nhập", 'Mã nhà cung cấp', 'Mã nhân viên', 'Sản phẩm', 'Giá', 'Số lượng', 'Ngày nhập']
        self.show_data(data, self.rec_table_view, header)

    @pyqtSlot()
    def on_rec_button_search_clicked(self):
        rec_search_id = self.rec_input_search.text().strip()
        receipt = Receipt(rec_search_id)
        search_query = receipt.search_data(receipt.id)
        rec_table = self.conn.execute_query(search_query)
        header = ["Mã phiếu nhập", 'Mã nhà cung cấp', 'Mã nhân viên', 'Sản phẩm', 'Giá', 'Số lượng', 'Ngày nhập']
        self.show_data(rec_table, self.rec_table_view, header)

    @pyqtSlot()
    def on_rec_button_add_clicked(self):
        cur = self.rec_table_view.rowCount()
        self.rec_table_view.insertRow(cur)

    def deli_show_data(self):
        show_query = "select de.iddelivery, de.idcustomer, de.iduser, dd.idproduct, dd.price, dd.quantity, de.date\
                    from delivery as de join deli_detail as dd on de.iddelivery = dd.iddelivery\
                    order by de.iddelivery asc;"
        data = self.conn.execute_query(show_query)
        header = ["Mã phiếu xuất", 'Mã KH', 'Mã nhân viên', 'Sản phẩm', 'Giá', 'Số lượng', 'Ngày xuất']
        self.show_data(data, self.deli_table_view, header)

    @pyqtSlot()
    def on_deli_button_search_clicked(self):
        deli_search_id = self.deli_input_search.text().strip()
        delivery = Delivery(deli_search_id)
        search_query = delivery.search_data(delivery.id)
        deli_table = self.conn.execute_query(search_query)
        header = ["Mã phiếu xuất", 'Mã KH', 'Mã nhân viên', 'Sản phẩm', 'Giá', 'Số lượng', 'Ngày xuất']
        self.show_data(deli_table, self.deli_table_view, header)

    @pyqtSlot()
    def on_deli_button_add_clicked(self):
        cur = self.deli_table_view.rowCount()
        self.deli_table_view.insertRow(cur)
        # pass

    def sup_show_data(self):
        show_query = "SELECT * FROM Suplier;"
        data = self.conn.execute_query(show_query)
        header = ["Mã NCC", 'Tên NCC', 'Email', 'Số điện thoại', 'Địa chỉ', 'Mã hợp đồng']
        self.show_data(data, self.sup_table_view, header)

    @pyqtSlot()
    def on_sup_button_search_clicked(self):
        sup_search_id = self.sup_input_search.text().strip()
        suplier = Suplier()
        search_query = suplier.search_data(sup_search_id)
        sup_table = self.conn.execute_query(search_query)
        header = ["Mã NCC", 'Tên NCC', 'Email', 'Số điện thoại', 'Địa chỉ', 'Mã hợp đồng']
        self.show_data(sup_table, self.sup_table_view, header)

    @pyqtSlot()
    def on_sup_button_add_clicked(self):
        cur = self.sup_table_view.rowCount()
        self.sup_table_view.insertRow(cur)

    def cus_show_data(self):
        show_query = "SELECT * FROM Customer;"
        data = self.conn.execute_query(show_query)
        header = ["Mã KH", 'Tên KH', 'Email', 'Số điện thoại', 'Địa chỉ', 'Mã hợp đồng']
        self.show_data(data, self.cus_table_view, header)

    @pyqtSlot()
    def on_cus_button_search_clicked(self):
        cus_search_id = self.cus_input_search.text().strip()
        customer = Customer()
        search_query = customer.search_data(cus_search_id)
        cus_table = self.conn.execute_query(search_query)
        header = ["Mã KH", 'Tên KH', 'Email', 'Số điện thoại', 'Địa chỉ', 'Mã hợp đồng']
        self.show_data(cus_table, self.cus_table_view, header)

    @pyqtSlot()
    def on_cus_button_add_clicked(self):
        cur = self.cus_table_view.rowCount()
        self.cus_table_view.insertRow(cur)

    def user_show_data(self):
        show_query = "SELECT * FROM User;"
        data = self.conn.execute_query(show_query)
        header = ["Mã NV", 'Họ và Tên', 'mật khẩu', 'Chức vụ']
        self.show_data(data, self.user_table_view, header)

    @pyqtSlot()
    def on_user_button_search_clicked(self):
        user_search_id = self.user_input_search.text().strip()
        user = User()
        search_query = user.search_data(user_search_id)
        user_table = self.conn.execute_query(search_query)
        header = ["Mã NV", 'Họ và Tên', 'mật khẩu', 'Chức vụ']
        self.show_data(user_table, self.user_table_view, header)

    @pyqtSlot()
    def on_user_button_add_clicked(self):
        cur = self.user_table_view.rowCount()
        self.user_table_view.insertRow(cur)

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
