import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase
import settings as st

class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        db = QSqlDatabase.addDatabase("QPSQL")
        db.setHostName(st.db_params["host"])
        db.setDatabaseName(st.db_params["dbname"])
        db.setPort(st.db_params["port"])
        db.setUserName(st.db_params["user"])
        db.setPassword(st.db_params["password"])
        ok = db.open()
        if ok:
            print("Connect to database", file=sys.stderr)
        else:
            print("Connection FAILED", file=sys.stderr)

if __name__ == "__main__":
    app = Application(sys.argv)
    sys.exit(app.exec_())


