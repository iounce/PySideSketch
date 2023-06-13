import sys
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6 import QtUiTools

form_type, base_type = QtUiTools.loadUiType('ch3_test.ui')

class MyLayoutWindow(base_type, form_type):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    win = MyLayoutWindow()
    win.resize(600, 300)
    win.show()

    sys.exit(app.exec())