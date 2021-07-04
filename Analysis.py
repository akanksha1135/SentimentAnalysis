import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from textblob import TextBlob

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Sentiment Analysis")
        self.btn = QPushButton("Quit", self)
        self.btn.setGeometry(QRect(80, 130, 113, 32))
        self.btn.setStyleSheet("background-color:red;\n"
                           "color: white;\n"
                           "border-style: outset;\n"
                           "border-width:2px;\n"
                           "border-radius:10px;\n"
                           "border-color:black;\n"
                           "font:bold 14px;\n"
                           "padding :6px;\n"
                           "min-width:10px;\n"
                           "\n"
                           "\n"
                           "")
        self.btn.clicked.connect(self.close_application)
        self.btn.move(400,50)
        self.btn2=QPushButton("Browse File", self)
        self.btn2.setGeometry(QRect(80, 130, 113, 32))
        self.btn2.setStyleSheet("background-color:red;\n"
                                      "color: white;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 14px;\n"
                                      "padding :6px;\n"
                                      "min-width:10px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.btn2.clicked.connect(self.pushButton_handler)
        self.btn2.move(400,0)
        self.label1 = QLabel('Positive', self)
        self.label1.move(150, 200)
        self.label1.setStyleSheet("background-color: yellow;border: 1px solid black;font:bold 14px;")
        self.label2 = QLabel('Neutral', self)
        self.label2.move(350, 200)
        self.label2.setStyleSheet("background-color: gray;border: 1px solid black;font:bold 14px;")
        self.label3 = QLabel('Negative', self)
        self.label3.move(550, 200)
        self.label3.setStyleSheet("background-color: red;border: 1px solid black;font:bold 14px;")
        self.textbox1 = QTextEdit(self)
        self.textbox1.move(150, 250)
        self.textbox1.resize(100, 100)
        self.textbox2 = QTextEdit(self)
        self.textbox2.move(350, 250)
        self.textbox2.resize(100, 100)
        self.textbox3 = QTextEdit(self)
        self.textbox3.move(550, 250)
        self.textbox3.resize(100, 100)

    def close_application(self):
        choice = QMessageBox.question(self, 'Extract!',
                                      "Do you want to exit?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def pushButton_handler(self):
        print("Button pressed")
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)
        #with open(path, "r") as f:
        file1 = open(path, 'r')
        Lines = file1.readlines()
        self.textbox1.clear()
        self.textbox2.clear()
        self.textbox3.clear()
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            blob=TextBlob(line)
            if blob.sentiment.polarity>0 :
                print(blob.sentiment.polarity)
                self.textbox1.append("Line{}\n".format(count))
            if blob.sentiment.polarity ==0:
                print(blob.sentiment.polarity)
                self.textbox2.append("Line{}\n".format(count))
            if blob.sentiment.polarity<0:
                print(blob.sentiment.polarity)
                self.textbox3.append("Line{}\n".format(count))
           # print("Line{}".format(count))


app = QApplication(sys.argv)

window = Window()
window.resize(1000,1000)
window.show()

app.exec_()