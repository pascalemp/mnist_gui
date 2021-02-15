import sys, os
import mnist_classifier as mclass
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import * 
from PyQt5 import QtCore 

class Example(QWidget):
    
    def __init__(self, screen_resolution):
        super().__init__()
        self.screen_resolution = screen_resolution
        self.l1 = QLabel(self)
        self.l2 = QLabel(self)
        self.l2.hide()
        self.l1.hide()
        self.initUI()

    def reset_button_handler(self):
        self.l1.hide()
        self.l2.hide()
        self.btn2.hide()
        self.btn.show() 
        self.repaint()

    def prediction_output_handler(self, prediction):
        prediction_text = 'Prediction = {}'.format(prediction)
        
        self.btn1.hide() 
        self.l2.setText(prediction_text)
        self.l2.show()
        self.btn2.show()        

    def prediction_handler(self):
        prediction = mclass.predict_image(self.file_path)[0]
        self.prediction_output_handler(prediction)

    def button_handler_open_file(self):

        self.file_path = QFileDialog.getOpenFileName()[0]
        filename = os.path.basename(self.file_path)

        if filename == '' or ('img_' not in filename):
            print('Nothing selected OR not a valid MNIST jpg file.')
        else:
            print('File: \'{}\' being selected!'.format(filename))
            
            im_pixmap = QPixmap(self.file_path)

            self.l1.setPixmap(im_pixmap)
            self.l1.setAlignment(QtCore.Qt.AlignCenter)
            self.l1.setGeometry(150-14,100-56,28,28)    
            self.l1.show()

            self.btn.hide()
            self.btn1.show()    

    def initUI(self):

        self.btn = QPushButton('Load Image', self)
        self.btn.setGeometry(150-75,150-30,150,60)        
        self.btn.clicked.connect(lambda: self.button_handler_open_file())
        
        self.btn1 = QPushButton(self)
        self.btn1.hide()
        self.btn1.setText('Predict')
        self.btn1.setGeometry(150-75,150-30,150,60)
        self.btn1.clicked.connect(lambda: self.prediction_handler())

        self.btn2 = QPushButton(self)
        self.btn2.hide()
        self.btn2.setText('Reset')
        self.btn2.setGeometry(150-75,150-30,150,60)
        self.btn2.clicked.connect(lambda: self.reset_button_handler())

        self.l2.setStyleSheet("background-color: lightgreen") 
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setGeometry(150-75,100-15,150,30)   
        
        self.setGeometry((self.screen_resolution.width()/2)-150, (self.screen_resolution.height()/2)-200, 300, 200)
        self.setFixedSize(self.size())
        self.setWindowTitle('MNIST Predictor')
        
        self.show()

def main():

    app = QApplication(sys.argv)
    screen_res = app.desktop().screenGeometry()
    ex = Example(screen_res)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()