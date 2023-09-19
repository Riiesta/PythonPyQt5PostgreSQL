from PyQt5.QtSql import QSqlQueryModel

class Model(QSqlQueryModel):
    def __int__(self, parent=None):
        super().__int__(parent)