import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
import multiprocessing

from src.Model.login import Login
from src.Control.control_main import Main


class LoginUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginUi, self).__init__()
        self.ui = uic.loadUi(r"View\login.ui", self)
        self.login_input_id = self.findChild(QtWidgets.QLineEdit, 'login_input_id')
        self.login_input_password = self.findChild(QtWidgets.QLineEdit, 'login_input_password')
        self.login_button = self.findChild(QtWidgets.QPushButton, 'login_button')
        self.login_button.clicked.connect(lambda: self.on_login_button_clicked)

    def on_login_button_clicked(self):
        login_input_id = self.login_input_id.text().strip()
        login_input_password = self.login_input_password.text().strip()

        user = Login()
        result = user.check_login(login_input_id, login_input_password)
        if result is False:
            title = "Đăng nhập không thành công"
            log = "Vui lòng kiểm tra lại thông tin"
            self.show_log(title, log)
        else:
            self.hide()
            window_main = Main()
            window_main.show()
            if result is True:
                window_main.tab.removeTab(5)

    @staticmethod
    def show_log(title, log):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(log)
        msg.setIcon(QMessageBox.Icon.Question)
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
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    window = LoginUi()
    window.show()
    sys.exit(app.exec())
