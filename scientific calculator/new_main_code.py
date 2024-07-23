import sys
from PyQt5 import QtWidgets
from curr_ui import Ui_MainWindow
from PyQt5.QtWidgets import  QMainWindow

label_data = ''

btnLarge_data = 'Rad | Deg'
btn1_2_data = 'x!'
btn1_3_data = '('
btn1_4_data = ')'
btn1_5_data = '%'
btn1_6_data = 'AC'

btn2_1_data = 'Inv'
btn2_2_data = 'sin'
btn2_3_data = 'ln'
btn2_4_data = 7
btn2_5_data = 8
btn2_6_data = 9
btn2_7_data = '÷'

btn3_1_data = 'π'
btn3_2_data = 'cos'
btn3_3_data = 'log'
btn3_4_data = 4
btn3_5_data = 5
btn3_6_data = 6
btn3_7_data = 'x'

btn4_1_data = 'e'
btn4_2_data = 'tan'
btn4_3_data = '√'
btn4_4_data = 1
btn4_5_data = 2
btn4_6_data = 3
btn4_7_data = '-'

btn5_1_data = 'Ans'
btn5_2_data = 'EXP'
btn5_3_data = 'x^y'
btn5_4_data = 0
btn5_5_data = '.'
btn5_6_data = '='
btn5_7_data = '+'

class BtnFunctionalities:
    def btnLarge_func(self):
        global label_data
        new_data = label_data + btnLarge_data
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn1_2_func(self):
        global label_data
        new_data = label_data + btn1_2_data
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn1_3_func(self):
        global label_data
        new_data = label_data + btn1_3_data
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn1_4_func(self):
        global label_data
        new_data = label_data + btn1_4_data
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn1_5_func(self):
        global label_data
        new_data = label_data + btn1_5_data
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn1_6_func(self):
        global label_data
        new_data = label_data + btn1_6_data
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn2_1_func(self):
        global label_data
        new_data = label_data + btn2_1_data
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn2_2_func(self):
        global label_data
        new_data = label_data + btn2_2_data
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn2_3_func(self):
        global label_data
        new_data = label_data + btn2_3_data
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn2_4_func(self):
        global label_data
        new_data = label_data + str(btn2_4_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn2_5_func(self):
        global label_data
        new_data = label_data + str(btn2_5_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn2_6_func(self):
        global label_data
        new_data = label_data + str(btn2_6_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn2_7_func(self):
        global label_data
        new_data = label_data + btn2_7_data
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn3_1_func(self):
        global label_data
        new_data = label_data + btn3_1_data
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn3_2_func(self):
        global label_data
        new_data = label_data + str(btn3_2_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn3_3_func(self):
        global label_data
        new_data = label_data + str(btn3_3_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn3_4_func(self):
        global label_data
        new_data = label_data + str(btn3_4_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn3_5_func(self):
        global label_data
        new_data = label_data + str(btn3_5_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn3_6_func(self):
        global label_data
        new_data = label_data + str(btn3_6_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn3_7_func(self):
        global label_data
        new_data = label_data + str(btn3_7_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn4_1_func(self):
        global label_data
        new_data = label_data + str(btn4_1_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn4_2_func(self):
        global label_data
        new_data = label_data + str(btn4_2_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn4_3_func(self):
        global label_data
        new_data = label_data + str(btn4_3_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn4_4_func(self):
        global label_data
        new_data = label_data + str(btn4_4_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn4_5_func(self):
        global label_data
        new_data = label_data + str(btn4_5_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn4_6_func(self):
        global label_data
        new_data = label_data + str(btn4_6_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn4_7_func(self):
        global label_data
        new_data = label_data + str(btn4_7_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn5_1_func(self):
        global label_data
        new_data = label_data + str(btn5_1_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn5_2_func(self):
        global label_data
        new_data = label_data + str(btn5_2_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn5_3_func(self):
        global label_data
        new_data = label_data + str(btn5_3_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn5_4_func(self):
        global label_data
        new_data = label_data + str(btn5_4_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
    def btn5_5_func(self):
        global label_data
        new_data = label_data + str(btn5_5_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn5_6_func(self):
        global label_data
        new_data = label_data + str(btn5_6_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)

    def btn5_7_func(self):
        global label_data
        new_data = label_data + str(btn5_7_data)
        label_data = new_data        
        self.displayLabel.setText(new_data)
    
class MainWindow(QMainWindow, Ui_MainWindow, BtnFunctionalities):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.initUI()

    def initUI(self):        
        # this will be connecting the functions with their respective buttons 

        # for all the number buttons we have connected the buttons with their respective functions 
        self.btnLarge.clicked.connect(self.btnLarge_func)
        self.btn1_2.clicked.connect(self.btn1_2_func)
        self.btn1_3.clicked.connect(self.btn1_3_func)
        self.btn1_4.clicked.connect(self.btn1_4_func)
        self.btn1_5.clicked.connect(self.btn1_5_func)
        self.btn1_6.clicked.connect(self.btn1_6_func)

        self.btn2_1.clicked.connect(self.btn2_1_func)
        self.btn2_2.clicked.connect(self.btn2_2_func)
        self.btn2_3.clicked.connect(self.btn2_3_func)
        self.btn2_4.clicked.connect(self.btn2_4_func)
        self.btn2_5.clicked.connect(self.btn2_5_func)
        self.btn2_6.clicked.connect(self.btn2_6_func)
        self.btn2_7.clicked.connect(self.btn2_7_func)

        self.btn3_1.clicked.connect(self.btn3_1_func)
        self.btn3_2.clicked.connect(self.btn3_2_func)
        self.btn3_3.clicked.connect(self.btn3_3_func)
        self.btn3_4.clicked.connect(self.btn3_4_func)
        self.btn3_5.clicked.connect(self.btn3_5_func)
        self.btn3_6.clicked.connect(self.btn3_6_func)
        self.btn3_7.clicked.connect(self.btn3_7_func)

        self.btn4_1.clicked.connect(self.btn4_1_func)
        self.btn4_2.clicked.connect(self.btn4_2_func)
        self.btn4_3.clicked.connect(self.btn4_3_func)
        self.btn4_4.clicked.connect(self.btn4_4_func)
        self.btn4_5.clicked.connect(self.btn4_5_func)
        self.btn4_6.clicked.connect(self.btn4_6_func)
        self.btn4_7.clicked.connect(self.btn4_7_func)

        self.btn5_1.clicked.connect(self.btn5_1_func)
        self.btn5_2.clicked.connect(self.btn5_2_func)
        self.btn5_3.clicked.connect(self.btn5_3_func)
        self.btn5_4.clicked.connect(self.btn5_4_func)
        self.btn5_5.clicked.connect(self.btn5_5_func)
        self.btn5_6.clicked.connect(self.btn5_6_func)
        self.btn5_7.clicked.connect(self.btn5_7_func)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
