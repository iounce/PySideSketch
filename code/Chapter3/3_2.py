import sys
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6 import QtUiTools
from ch3_test import Ui_MainWindow

class MyLayoutWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    win = MyLayoutWindow()
    win.resize(600, 300)
    win.show()

    sys.exit(app.exec())