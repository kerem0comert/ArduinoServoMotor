# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Anka_Gui_Mk1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from socket import socket
from Socket import Socket
from tkinter import Tk, Frame, Label, Button, HORIZONTAL, VERTICAL, Scale
from VideoStreamThread import VideoStreamThread
from numpy import interp
import Joystick

class PositionSlider(QtWidgets.QSlider):
    def __init__(self, parent: QtWidgets.QWidget, dataType: str, _from: int, to: int):
        QtWidgets.QSlider.__init__(self, parent=parent)
        self.setMinimum(_from)
        self.setMaximum(to)
        self.dataType = dataType
        self.valueChanged.connect(self.updateValue)
        
    def updateValue(self):
        self.printAngle()
        sendData(self.value())
    
    def printAngle(self): print(f"Angle = {self.value()} {self.dataType}")
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gViewCameraFeed = QtWidgets.QGraphicsView(self.centralwidget)
        self.gViewCameraFeed.setGeometry(QtCore.QRect(260, 40, 640, 480))
        self.gViewCameraFeed.setObjectName("Lb_camera_feed")
        self.gViewMinimap = QtWidgets.QGraphicsView(self.centralwidget)
        self.gViewMinimap.setGeometry(QtCore.QRect(0, 531, 251, 181))
        self.gViewMinimap.setObjectName("Lb_minimap")
        self.bAction2 = QtWidgets.QPushButton(self.centralwidget)
        self.bAction2.setGeometry(QtCore.QRect(60, 40, 131, 31))
        self.bAction2.setObjectName("Lb_action_2")
        self.bAction3 = QtWidgets.QPushButton(self.centralwidget)
        self.bAction3.setGeometry(QtCore.QRect(60, 90, 131, 31))
        self.bAction3.setObjectName("Lb_action_3")
        self.bAction4 = QtWidgets.QPushButton(self.centralwidget)
        self.bAction4.setGeometry(QtCore.QRect(60, 140, 131, 31))
        self.bAction4.setObjectName("Lb_action_4")
        self.bAction5 = QtWidgets.QPushButton(self.centralwidget)
        self.bAction5.setGeometry(QtCore.QRect(60, 190, 131, 31))
        self.bAction5.setObjectName("Lb_action_5")
        self.bAction6 = QtWidgets.QPushButton(self.centralwidget)
        self.bAction6.setGeometry(QtCore.QRect(60, 240, 131, 31))
        self.bAction6.setObjectName("Lb_action_6")
        
        self.slHrzCamera = QtWidgets.QSlider(self.centralwidget)
        self.slHrzCamera.setGeometry(QtCore.QRect(40, 310, 160, 22))
        self.slHrzCamera.setSliderPosition(50)
        self.slHrzCamera.setOrientation(QtCore.Qt.Horizontal)
        self.slHrzCamera.setObjectName("Lb_camera_horizantal")
        self.slVrtCamera = QtWidgets.QSlider(self.centralwidget)
        self.slVrtCamera.setGeometry(QtCore.QRect(210, 340, 22, 160))
        self.slVrtCamera.setSliderPosition(50)
        self.slVrtCamera.setOrientation(QtCore.Qt.Vertical)
        self.slVrtCamera.setObjectName("Lb_camera_vertical")
        
        self.slVrtMovement = PositionSlider(parent=self.centralwidget, dataType='t', _from=-90, to=90)
        self.slVrtMovement.setGeometry(QtCore.QRect(1080, 350, 22, 160))
        self.slVrtMovement.setSliderPosition(50)
        self.slVrtMovement.setOrientation(QtCore.Qt.Vertical)
        self.slVrtMovement.setObjectName("Lb_movement_vertical")
        
        self.slHrzMovement = PositionSlider(parent=self.centralwidget, dataType='p', _from=90, to=-30)
        self.slHrzMovement.setGeometry(QtCore.QRect(930, 310, 160, 22))
        self.slHrzMovement.setSliderPosition(50)
        self.slHrzMovement.setOrientation(QtCore.Qt.Horizontal)
        self.slHrzMovement.setObjectName("Lb_movement_horizantal")
        
        self.Lb_output_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.Lb_output_1.setGeometry(QtCore.QRect(920, 40, 181, 51))
        self.Lb_output_1.setObjectName("Lb_output_1")
        self.Lb_output_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Lb_output_2.setGeometry(QtCore.QRect(920, 110, 181, 51))
        self.Lb_output_2.setObjectName("Lb_output_2")
        self.Lb_output_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.Lb_output_3.setGeometry(QtCore.QRect(920, 180, 181, 51))
        self.Lb_output_3.setObjectName("Lb_output_3")
        self.Lb_output_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.Lb_output_4.setGeometry(QtCore.QRect(920, 240, 181, 51))
        self.Lb_output_4.setObjectName("Lb_output_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 530, 641, 121))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 659, 641, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.Lb_joystick_widget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.Lb_joystick_widget.setGeometry(QtCore.QRect(910, 530, 201, 181))
        self.Lb_joystick_widget.setObjectName("Lb_joystick_widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bAction2.setText(_translate("MainWindow", "PushButton"))
        self.bAction3.setText(_translate("MainWindow", "PushButton"))
        self.bAction4.setText(_translate("MainWindow", "PushButton"))
        self.bAction5.setText(_translate("MainWindow", "PushButton"))
        self.bAction6.setText(_translate("MainWindow", "PushButton"))
        
    def initVideoStream(self, MainWindow):
        self.videoStream = VideoStreamThread(self.gViewCameraFeed, STREAM_HOST)
        self.videoStream.start()

    def initJoystick(self): pass


WINDOWS_HOST = "192.168.1.107"
STREAM_HOST = 'http://192.168.1.34:8081/'
RASPBERRY_PORT = 5000
BAUD_RATE = 9600

def sendData(data, dataType):
    if dataType == 't': data = int(interp(data, [-90,90], [180,0]))
    elif dataType == 'p': data = int(interp(data, [-30,90], [120,0]))
    else: 
        if data < 0: dataType = 's' #in the case of 'w' datatype, a negative value will indicate 's' for backwards
        data =  int(interp(abs(data), [0,100], [40,255]))
 
    #make sure data has 3 digits
    if(data < 10): data = "00" + str(data)
    elif(data < 100): data = "0" + str(data)
    else:  data = str(data)
    
    toSend = str(data) + str(dataType)
    print(toSend)
    connection.send(repr(toSend).encode('utf-8'))

if __name__ == "__main__":
    socketInstance = Socket(WINDOWS_HOST, RASPBERRY_PORT)
    print("Listening...")
    connection, address = socketInstance.startListening()
    print (f"Connection from: {str(address)}")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #app.initVideoStream(STREAM_HOST)
    while 1:
        app.initJoystick()
        data = connection.recv(BAUD_RATE).decode()
        if not data: break 
        print(f"From raspberry pi: {str(data)}")
        app.root.mainloop()
    connection.close()
    sys.exit(app.exec_())
    