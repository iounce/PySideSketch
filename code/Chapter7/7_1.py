import sys
from PySide6 import QtWidgets, QtGui

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        exit_action = QtGui.QAction('&Exit', self)
        exit_action.triggered.connect(self.close)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    win = MyWindow()
    win.resize(600, 300)
    win.show()

    sys.exit(app.exec())