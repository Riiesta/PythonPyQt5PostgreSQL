import sys
from PyQt5.QtWidgets import QApplication
from Application import Application
from MainWindow import MainWindow

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

sys.exit(app.exec_())
