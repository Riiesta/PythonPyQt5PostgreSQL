from PyQt5.QtWidgets import QTableView, QMessageBox
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import pyqtSlot

class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        sql = "" \
              "select id, f_fio, f_phone, f_email, f_comment" \
              "from techer;"
        self.setQuery(sql)

class View(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

        model = Model(parent=self)
        self.setModel(model)

    @pyqtSlot()
    def add(self):
        dia = Dialog(parent=self)
        dia.exec()
        #QMessageBox.information(self, "Учитель", "Добавление")

    @pyqtSlot()
    def update(self):
        QMessageBox.information(self, "Учитель", "Редактирование")

    @pyqtSlot()
    def delete(self):
        QMessageBox.information(self, "Учитель", "Удаление")

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        fio_lbl = QLabel("Фамилия И.О.")
        self.__fio_edt = QLineEdit(parent=self)

        phone_lbl = QLabel("Телефон")
        self.__phone_edt = QLineEdit(parent=self)

        email_lbl = QLabel("e-mail")
        self.__email_edt = QLineEdit(parent=self)

        comment_lbl = QLabel("Примечание")
        self.__comment_edt = QTextEdit(parent=self)

        ok_btn = QPushButton("ОК", parent=self)
        cancel_btn = QPushButton("Отмена", parent=self)

        lay = QVBoxLayout(self)
        lay.addWidget(fio_lbl)
        lay.addWidget(self.fio_edt)
        lay.addWidget(phone_lbl)
        lay.addWidget(self.phone_edt)
        lay.addWidget(email_lbl)
        lay.addWidget(self.email_edt)
        lay.addWidget(comment_lbl)
        lay.addWidget(self.comment_edt)

        lay2 = QHBoxLayout()
        lay2.addWidget(ok_btn)
        lay2.addWidget(cancel_btn)
        lay2.addLayout(lay2)

        cancel_btn.clicked.connect(self.reject)


