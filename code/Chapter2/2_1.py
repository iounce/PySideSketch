import sys
from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    win = QtWidgets.QWidget()
    win.resize(600, 300)
    win.show()

    sys.exit(app.exec())