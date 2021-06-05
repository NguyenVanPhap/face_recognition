##nhap
#import numpy as np
#import cv2
#import numpy as np
#import sqlite3
#from GetImageToData import *
#from Train_Data import *

#def Recognie():
#    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#    eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#    cap = cv2.VideoCapture(0)

#    fourcc = cv2.VideoWriter_fourcc(*'XVID')
#    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

#    while (True):
#        ret, frame = cap.read()
#        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#        faces = face_cascade.detectMultiScale(gray)
#        for (x, y, w, h) in faces:
#            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#            roi_gray = gray[y:y + h, x:x + w]
#            roi_color = frame[y:y + h, x:x + w]

#            eyes = eyeCascade.detectMultiScale(
#                roi_gray,
#                scaleFactor=1.5,
#                minNeighbors=10,
#                minSize=(5, 5),
#            )

#            for (ex, ey, ew, eh) in eyes:
#                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
#            smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
#            for (sx, sy, sw, sh) in smiles:
#                # Draw the rectangle around every eye
#                cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
#        out.write(frame)
#        cv2.imshow('Camera - Nguyen Phap', frame)
#        if cv2.waitKey(1) & 0xFF == ord('q'):
#            break

#    cap.release()
#    out.release()
#    cv2.destroyAllWindows()

from PyQt5 import QtCore, QtGui, QtWidgets
from GetInfor_ui import *
from Train_Data import*
from FaceRecognier import *

import pandas as pd
s = pd.Series([0,1,2,3])
class Ui_MainWindow(object):
    def OpenGetInforWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_EnterID()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        def ClickRoll(self):
            Recognize()


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 745)
        MainWindow.setStyleSheet("background-color:#111111")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 171, 721))
        self.frame.setStyleSheet("Background-color:#222222")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnGetID = QtWidgets.QPushButton(self.frame)
        self.btnGetID.setGeometry(QtCore.QRect(0, 210, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnGetID.setFont(font)
        self.btnGetID.setStyleSheet("QPushButton {\n"
                "    color: rgb(255, 255, 255);\n"
                "    background-color:#777777;\n"
                "    border: 0px solid;\n"
                "}\n"
                "QPushButton:hover {\n"
                "    background-color: rgb(85, 170, 255);\n"
                "}")
        self.btnGetID.setObjectName("btnGetID")
        self.btnGetID.clicked.connect(self.OpenGetInforWindow)

        self.btnTrain = QtWidgets.QPushButton(self.frame)
        self.btnTrain.setGeometry(QtCore.QRect(0, 290, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnTrain.setFont(font)
        self.btnTrain.setStyleSheet("QPushButton {\n"
                "    color: rgb(255, 255, 255);\n"
                "    background-color:#777777;\n"
                "    border: 0px solid;\n"
                "}\n"
                "QPushButton:hover {\n"
                "    background-color: rgb(85, 170, 255);\n"
                "}")
        self.btnTrain.setObjectName("btnTrain")
        self.btnTrain.clicked.connect(TrainData)
        self.btnRC = QtWidgets.QPushButton(self.frame)
        self.btnRC.setGeometry(QtCore.QRect(0, 370, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRC.setFont(font)
        self.btnRC.setStyleSheet("QPushButton {\n"
                "    color: rgb(255, 255, 255);\n"
                "    background-color:#777777;\n"
                "    border: 0px solid;\n"
                "}\n"
                "QPushButton:hover {\n"
                "    background-color: rgb(85, 170, 255);\n"
                "}")
        self.btnRC.setObjectName("btnRC")
        self.btnRC.clicked.connect(Recognize)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 20, 171, 151))
        self.label.setFrameShape(QtWidgets.QFrame.VLine)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/PC/Downloads/creative-vector-illustration-biometric-face-verification-scan-identification-scanning-system-background-art-design-high-te-129676929.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 630, 171, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/PC/Downloads/ssg.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(190, 10, 311, 721))
        self.widget.setStyleSheet("Background-color:#222222")
        self.widget.setObjectName("widget")
        self.lstwtID = QtWidgets.QListWidget(self.widget)
        self.lstwtID.setGeometry(QtCore.QRect(10, 20, 291, 691))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lstwtID.setFont(font)
        self.lstwtID.setStyleSheet("background:white")
        self.lstwtID.setViewMode(QtWidgets.QListView.ListMode)
        self.lstwtID.setModelColumn(0)
        self.lstwtID.setObjectName("lstwtID")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Điểm danh"))
        self.btnGetID.setText(_translate("MainWindow", "Get ID"))
        self.btnTrain.setText(_translate("MainWindow", "Machine Training"))
        self.btnRC.setText(_translate("MainWindow", "Rooling Call"))
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    