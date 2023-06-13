import sys
from PySide6 import QtWidgets, QtCore
import qt_material

class MyMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QtWidgets.QGridLayout(self)
        hello_layout = QtWidgets.QVBoxLayout()
        world_layout = QtWidgets.QVBoxLayout()

        self.grid_layout.addLayout(hello_layout, 0, 0, 1, 2)
        self.grid_layout.addLayout(world_layout, 1, 0, 1, 2)

        hello_btn = QtWidgets.QPushButton(self)
        hello_btn.setText("Click me")
        hello_btn.clicked.connect(self.show_menu)
        hello_layout.addWidget(hello_btn)

        world_lbl = QtWidgets.QLabel(self)
        world_layout.addWidget(world_lbl)
        
        self.data_widget = world_lbl
        
    def show_menu(self):
        win = MySubWindow(self)
        win.resize(300, 200)
        win.data_signal.connect(self.on_signal)
        win.show()
        
    def on_signal(self, msg):
        print(msg)
        self.data_widget.setText(msg)

class MySubWindow(QtWidgets.QDialog):
    data_signal = QtCore.Signal(str)
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.signal_btn = QtWidgets.QPushButton(self)
        self.signal_btn.setText("Send message")
        self.signal_btn.clicked.connect(self.send_msg)
        self.count = 0
        
    def send_msg(self):
        self.count += 1
        self.data_signal.emit("Signal here: " + str(self.count))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    qt_material.apply_stylesheet(app, 'dark_blue.xml')
    
    win = MyMainWindow()
    win.resize(600, 300)
    win.show()

    sys.exit(app.exec())