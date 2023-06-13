import sys
from PySide6 import QtWidgets

class MyLayoutWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QtWidgets.QGridLayout(self)
        hello_layout = QtWidgets.QVBoxLayout()
        world_layout = QtWidgets.QVBoxLayout()
        
        self.grid_layout.addLayout(hello_layout, 0, 0, 1, 2)
        self.grid_layout.addLayout(world_layout, 1, 0, 1, 2)
        
        hello_label = QtWidgets.QLabel(self)
        hello_label.setText("Hello")
        hello_layout.addWidget(hello_label)
        
        world_label = QtWidgets.QLabel(self)
        world_label.setText("World")
        world_layout.addWidget(world_label)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    win = MyLayoutWindow()
    win.resize(600, 300)
    win.show()

    sys.exit(app.exec())