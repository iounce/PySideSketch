import sys
from PySide6 import QtWidgets, QtCore
import qt_material

class MyMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    translator = QtCore.QTranslator()
    translator.load('zh_CN')
    
    app = QtWidgets.QApplication([])
    
    app.installTranslator(translator)

    qt_material.apply_stylesheet(app, 'dark_blue.xml')
    
    win = MyMainWindow()
    win.resize(600, 300)
    win.show()

    sys.exit(app.exec())
