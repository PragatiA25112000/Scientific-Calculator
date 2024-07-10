import sys
from PyQt5 import QtWidgets
from ui2 import Ui_MainWindow  # Assuming your generated UI file is named ui2.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.curr_ui = Ui_MainWindow()
        self.curr_ui.setupUi(self)
        self.curr_ui.retranslateUi(self)

        self.initUI()
        print("printing the id of self: ", id(self))

    def initUI(self):
        self.curr_ui.pushButton1.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # Example function to handle button click
        QtWidgets.QMessageBox.information(self, "Message", "Button clicked!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    print("printing the id of  mainWindow object :: ", id(mainWindow))
    mainWindow.show()
    sys.exit(app.exec_())
