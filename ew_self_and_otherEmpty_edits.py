#Imports all necessary packages to run the experiment
from PyQt4 import QtCore, QtGui
import threading, sys
import time, os, InstrumentControl, datetime
import random
import cv2
import numpy as np
from numpy import *
from CameraGUI import ShowVideo, ImageViewer
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#The following section controls the generation of the GUI. Only the relevant code
#that may need to be changed will be commented.
#-------------------------------------------------------------------------------
try:
    import Queue
except:
    import queue as Queue
    
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
running = 0
class Ui_EmpathyTrialGUI(object):
    def setupUi(self, EmpathyTrialGUI):
        EmpathyTrialGUI.setObjectName(_fromUtf8("EmpathyTrialGUI"))
        EmpathyTrialGUI.resize(844, 283)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0) 
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EmpathyTrialGUI.sizePolicy().hasHeightForWidth())
        EmpathyTrialGUI.setSizePolicy(sizePolicy)
        EmpathyTrialGUI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(EmpathyTrialGUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.Icon = QtGui.QLabel(self.centralwidget) 
        self.image = QtGui.QImage()
        self.Icon.setText(_fromUtf8(""))
        self.Icon.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/ICON.bmp")))
        self.Icon.setObjectName(_fromUtf8("Icon"))
        self.verticalLayout_4.addWidget(self.Icon)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)
        self.Madeby = QtGui.QLabel(self.centralwidget)
        self.Madeby.setObjectName(_fromUtf8("Madeby"))
        self.verticalLayout_4.addWidget(self.Madeby)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.StartTimer = QtGui.QLCDNumber(self.centralwidget)
        self.StartTimer.setFrameShadow(QtGui.QFrame.Plain)
        self.StartTimer.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.StartTimer.setObjectName(_fromUtf8("StartTimer"))
        self.gridLayout.addWidget(self.StartTimer, 2, 0, 1, 1)

        self.Temp = QtGui.QLCDNumber(self.centralwidget)  # Temp display
        self.Temp.setFrameShadow(QtGui.QFrame.Plain)
        self.Temp.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Temp.setObjectName(_fromUtf8("Temp"))
        self.gridLayout.addWidget(self.Temp, 4, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout.addWidget(self.lcdNumber, 2, 1, 1, 1)

        self.trialcounter = QtGui.QLCDNumber(self.centralwidget)  
        self.trialcounter.setFrameShadow(QtGui.QFrame.Plain)
        self.trialcounter.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.trialcounter.setObjectName(_fromUtf8("trialcounter"))
        self.gridLayout.addWidget(self.trialcounter, 4, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_13, 3, 1, 1, 1)
        
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/pic1.png")))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.UserInput = QtGui.QLineEdit(self.centralwidget)
        self.UserInput.setObjectName(_fromUtf8("UserInput"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.UserInput)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.ActiveInput = QtGui.QLineEdit(self.centralwidget)
        self.ActiveInput.setText(_fromUtf8(""))
        self.ActiveInput.setObjectName(_fromUtf8("ActiveInput"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.ActiveInput)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.PassiveInput = QtGui.QLineEdit(self.centralwidget)
        self.PassiveInput.setText(_fromUtf8(""))
        self.PassiveInput.setObjectName(_fromUtf8("PassiveInput"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.PassiveInput)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.StageNum = QtGui.QComboBox(self.centralwidget)
        self.StageNum.setObjectName(_fromUtf8("StageNum"))
        # number of possible stages in GUI
        self.StageNum.addItem(_fromUtf8(""))
        self.StageNum.addItem(_fromUtf8(""))
        self.StageNum.addItem(_fromUtf8(""))
        self.StageNum.addItem(_fromUtf8(""))
        self.StageNum.addItem(_fromUtf8(""))
        #added
        self.StageNum.addItem(_fromUtf8(""))
        self.StageNum.addItem(_fromUtf8(""))
        self.StageNum.addItem(_fromUtf8(""))
        self.StageNum.addItem(_fromUtf8(""))
        self.StageNum.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.StageNum)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.TrialNum = QtGui.QLineEdit(self.centralwidget)
        self.TrialNum.setObjectName(_fromUtf8("TrialNum"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.TrialNum)

        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_14)
        self.delaytime = QtGui.QLineEdit(self.centralwidget)
        self.delaytime.setObjectName(_fromUtf8("TrialNum"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.delaytime)
        
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.NameInput = QtGui.QLineEdit(self.centralwidget)
        self.NameInput.setText(_fromUtf8(""))
        self.NameInput.setObjectName(_fromUtf8("NameInput"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.NameInput)
        self.verticalLayout.addLayout(self.formLayout)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.TrialStart = QtGui.QPushButton(self.centralwidget)
        self.TrialStart.setObjectName(_fromUtf8("TrialStart"))  
        self.verticalLayout.addWidget(self.TrialStart)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        
        EmpathyTrialGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmpathyTrialGUI)
        QtCore.QMetaObject.connectSlotsByName(EmpathyTrialGUI)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.GUIManager)

    def retranslateUi(self, EmpathyTrialGUI):
        EmpathyTrialGUI.setWindowTitle(_translate("EmpathyTrialGUI", "EmpathyTrialGUI", None))
        self.Madeby.setText(_translate("EmpathyTrialGUI", "Created and Developed by: Teryn Johnson", None))
        self.label_10.setText(_translate("EmpathyTrialGUI", "Seconds Since Trial Start:", None))
        self.label_9.setText(_translate("EmpathyTrialGUI", "Seconds Since Experiment Start:", None))
        self.label_8.setText(_translate("EmpathyTrialGUI", "Experimental Parameter Input:", None))
        self.label_11.setText(_translate("EmpathyTrialGUI", "Current Temperature:", None))  # Temp display
        self.label_13.setText(_translate("EmpathyTrialGUI", "Trial Number:", None))
        self.label_14.setText(_translate("EmpathyTrialGUI", "Delay Time:", None))
        self.label_6.setText(_translate("EmpathyTrialGUI", "User:", None))
        self.UserInput.setText(_translate("EmpathyTrialGUI", "Nicole", None))
        self.label_2.setText(_translate("EmpathyTrialGUI", "Active Rat ID:", None))
        self.label_3.setText(_translate("EmpathyTrialGUI", "Passive Rat ID:", None))
        self.label.setText(_translate("EmpathyTrialGUI", "Stage Number:", None))
        # creates the availible stage names for drop down menu in GUI
        self.StageNum.setItemText(0, _translate("EmpathyTrialGUI", "11", None))
        self.StageNum.setItemText(1, _translate("EmpathyTrialGUI", "12", None))
        self.StageNum.setItemText(2, _translate("EmpathyTrialGUI", "21", None))
        self.StageNum.setItemText(3, _translate("EmpathyTrialGUI", "22", None))
        self.StageNum.setItemText(4, _translate("EmpathyTrialGUI", "23", None))
        #added code
        self.StageNum.setItemText(5, _translate("EmpathyTrialGUI", "24", None))
        self.StageNum.setItemText(6, _translate("EmpathyTrialGUI", "31", None))
        self.StageNum.setItemText(7, _translate("EmpathyTrialGUI", "32", None))
        self.StageNum.setItemText(8, _translate("EmpathyTrialGUI", "33", None))
        self.StageNum.setItemText(9, _translate("EmpathyTrialGUI", "34", None))
        
        self.pushButton.setText(_translate("EmpathyTrialGUI", "?", None))
        self.label_4.setText(_translate("EmpathyTrialGUI", "# of Trials:", None))
        # self.TrialNum.setText(_translate("EmpathyTrialGUI", "10", None))
        self.label_7.setText(_translate("EmpathyTrialGUI", "Filename:", None))
        self.TrialStart.setText(_translate("EmpathyTrialGUI", "Start Trial", None))
        self.pushButton_2.setText(_translate("EmpathyTrialGUI", "End Current Trial", None))
        self.TrialStart.clicked.connect(self.experimentrun)
        self.pushButton.clicked.connect(self.helpmessage)
        self.pushButton_2.clicked.connect(self.skiptrial)

#End GUI generation portion of the code
#-------------------------------------------------------------------------------

    #This controls the message that is displayed when the help button is clicked
    #on the GUI
    def helpmessage(self):
        print "1 - Shaping Protocol (One nose port, air on middle chamber)"
        print "2 - Testing Protocol (Two nose ports, air on middle and left chamber)"

    #This controls the actual run of the experiment. When the "Start Trial" button
    #is clicked, it runs this script.
    def experimentrun(self):
        os.chdir('C:\Users\Chiba Lab\Desktop\Data') #Changes file save location
        global experimentseconds, trialseconds, savename, camera, cameraoutput, timestamp
        #Pulls all information from the input windows on GUI
        activerat = self.ActiveInput.text()
        passiverat = self.PassiveInput.text()
        savename = self.NameInput.text()
        user = self.UserInput.text()
        num = int(self.TrialNum.text())
        stage = str(self.StageNum.currentText())
        delay = int(self.delaytime.text())
        if ((int(stage) == 11 or int(stage) == 12 or int(stage) == 21 or int(stage) == 22 or int(stage) == 23 or int(stage) == 24 or int(stage) == 31 or int(stage) ==32 or int(stage) ==33 or int(stage) == 34 or int(stage) == 6 and num % 2 == 0) or int(stage) == 1): #Ensures that stage 2 and 3 saves properly
            #Connects the camera to the GUI and starts recording
            camera = cv2.VideoCapture(0)
            camera.set(3, 1920)
            camera.set(4, 1080)
            #camera.set(3, 4096)
            #camera.set(4, 2160)
            time.sleep(2)
            #camera.set(3, 1280)
            #camera.set(4, 720)
            camera.set(5, 15.0)
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            vid_name = str(savename)+'.avi'
            #cameraoutput = cv2.VideoWriter(vid_name, fourcc, 30.0, (640,480))
            cameraoutput = cv2.VideoWriter(vid_name, fourcc, 15.0, (1920,1080))
            #cameraoutput = cv2.VideoWriter(vid_name, fourcc, 15.0, (4096,2160))
            self.Pacer() #Starts the "pacing" for the experiment timing
            experimentseconds = 0
            trialseconds = 0
            #Starts the experiment on a seperate thread. Necessary for parallel processing
            experimentthread = threading.Thread(None, self.experiment, None, (activerat, passiverat, savename, user, num, stage,delay))
            experimentthread.start()
            timestamp = []
            #tempthread = threading.Thread(None, self.temperaturesave, None, ())
            #tempthread.start()
        elif (int(stage) == 7 and num % 3 == 0):
            #Connects the camera to the GUI and starts recording
            camera = cv2.VideoCapture(0)
            camera.set(3, 1920)
            camera.set(4, 1080)
            #camera.set(3, 4096)
            #camera.set(4, 2160)
            time.sleep(2)
            #camera.set(3, 1280)
            #camera.set(4, 720)
            camera.set(5, 15.0)
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            vid_name = str(savename)+'.avi'
            #cameraoutput = cv2.VideoWriter(vid_name, fourcc, 30.0, (640,480))
            cameraoutput = cv2.VideoWriter(vid_name, fourcc, 15.0, (1920,1080))
            #cameraoutput = cv2.VideoWriter(vid_name, fourcc, 15.0, (4096,2160))
            self.Pacer() #Starts the "pacing" for the experiment timing
            experimentseconds = 0
            trialseconds = 0
            #Starts the experiment on a seperate thread. Necessary for parallel processing
            experimentthread = threading.Thread(None, self.experiment, None, (activerat, passiverat, savename, user, num, stage,delay))
            experimentthread.start()
            timestamp = []
            #tempthread = threading.Thread(None, self.temperaturesave, None, ())
            #tempthread.start()
        else:
            print "The number of trials for stage 2, 3, 4, 5, and 6 must be an even number"
            print "7 must be divisable by 3."

    #This controls the end current trial button.
    def skiptrial(self):
        global IRsensorque
        IRsensorque.put(30)

    #This continuously checks the arduino board for sensor signals.
    def sensorcheck(self):
        global StepperControl
        Trig = 0
        while Trig != 25:
            Trig = int(StepperControl.LeverCheck())
            if Trig == 5:
                IRsensorque.put(5)
            elif Trig == 10:
                IRsensorque.put(10)
            elif Trig == 15:
                IRsensorque.put(15)
            elif Trig == 20:
                IRsensorque.put(20)
            elif Trig == 50:
                IRsensorque.put(50)
            elif Trig == 100:
                IRsensorque.put(100)
            elif Trig == 150:
                IRsensorque.put(150)
            elif Trig == 200:
                IRsensorque.put(200)
    #This is responsible for recording the temperature of the box throughout the experiment
    #def temperaturesave(self):
        #global Stepper1, experimentendque, savename
        #file_object3=open(savename + '_temp.txt','w')
        #end = 0
        #tempcount = 0
        #while end != 1:
            #tempq = Stepper1.LeverCheck()
            #tempcount = tempcount + 1
            #if tempq != '':
                #print >> file_object3, tempq,
                #if tempcount > 10:
                    #self.Temp.setDigitCount(len(tempq))
                    #self.Temp.display(tempq)
                    #tempcount = 0
            #if(not experimentendque.empty()):
                #end = experimentendque.get()
        #file_object3.close()

    #This paces the experiment by seconds. Used for the timers.      
    def Pacer(self):
        global experimentseconds
        experimentseconds = 0 
        self.timer.start(1)

    #This controls everything related to the GUI
    def GUIManager(self):
        global imageque, timestamp, timerthread, camera, cameraoutput
        #This controls the image that is displayed on the GUI
        if(not imageque.empty()):
            imageID = imageque.get()
            if(imageID ==0):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_CENTER_cartoon_template.png")))
            elif(imageID == 1):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_CENTER_all_red.png")))
            elif(imageID == 2):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_CENTER_user_end_bottom_left.png")))
            elif(imageID == 3):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_CENTER_user_end_bottom_right.png")))
            elif(imageID == 4):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_CENTER_user_end_top_left.png")))
            elif(imageID == 5):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_CENTER_user_end_top_right.png")))
            elif(imageID == 6):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_LEFT_all_red.png")))
            elif(imageID == 7):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_LEFT_bottom_left.png")))
            elif(imageID == 8):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_LEFT_bottom_right.png")))
            elif(imageID == 9):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_LEFT_top_left.png")))
            elif(imageID == 10):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_LEFT_top_right.png")))
            elif(imageID == 11):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_RIGHT_all_red.png")))
            elif(imageID == 12):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_RIGHT_bottom_left.png")))
            elif(imageID == 13):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_RIGHT_bottom_right.png")))
            elif(imageID == 14):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_RIGHT_top_left.png")))
            elif(imageID == 15):
                self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Python27/Lib/site-packages/PyQt4/Resources/dual_nosepoke_RIGHT_top_right.png")))
        timestamp = []
        #This controls the experiment timer
        if(not experimentcountque.empty()):
            exphold = experimentcountque.get()
            timehold1 = "{0}".format(exphold)
            timestamp.append(str(timehold1))
            self.StartTimer.setDigitCount(len(timehold1))
            self.StartTimer.display(timehold1)
        #This controls the trial timer
        if(not trialcountque.empty()):
            trialhold = trialcountque.get()
            timehold2 = "{0}".format(trialhold)
            self.lcdNumber.setDigitCount(len(timehold2))
            self.lcdNumber.display(timehold2)

        if(not timerthread.empty()):
            self.timer.stop()

        #This controls the camera display on the GUI
        ret, image = camera.read()
        cameraoutput.write(image)
        resized_image = cv2.resize(image, (1280,720))
        #resized_image = cv2.resize(image, (640,480))
        color_swapped_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
        height, width, channel = color_swapped_image.shape
        bytesPerLine = 3 * width
        QImg = QtGui.QImage(color_swapped_image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        #QImg = QtGui.QImage(resized_image.data, 640, 480, bytesPerLine, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(QImg)
        self.Icon.setPixmap(pixmap)

    #This is the definition that controls the pacing for the experiment timer
    def ExperimentTime(self):
        global experimenttimeque, experimentseconds, experimentcountque
        experimentstop = 0
        while experimentstop != 1:
            if(not experimenttimeque.empty()):
                experimentstop = experimenttimeque.get()
            time.sleep(1)
            experimentseconds += 1
            experimentcountque.put(experimentseconds)

    #This is the definition that controls the pacing for the trial timer
    def Trialtime(self):
        global trialtimeque, trialseconds, trialcountque
        trialstop = 0
        trialseconds = 0
        while trialstop != 2:
            if(not trialtimeque.empty()):
                trialstop = trialtimeque.get()
            time.sleep(1)
            trialseconds += 1
            trialcountque.put(trialseconds)

    #This is the definition that controls the actual control of the experiment
    def experiment(self, activerat, passiverat, savename, user, trialnum, stagenum,delay):
        global imageque, StepperControl, experimenttimethread, count, cameraoutput, camera
        savefilespacing = 10
        #Starts the thread responsible for looking at the sensor.
        sensorthread = threading.Thread(None, self.sensorcheck, None, ())
        sensorthread.start()

        experimenttimestart = str(datetime.datetime.now())

        #Creates the files used for saving the data and saves all relevant information
        #in the header file.
        datafile=open(savename + '.txt','w')
        headerfile=open(savename + '.hdr','w')
        print >> headerfile, savename
        print >> headerfile, experimenttimestart
        print >> headerfile, 'User:'
        print >> headerfile, user
        print >> headerfile, 'Stage Number:'
        print >> headerfile, stagenum
        print >> headerfile, 'Active Rat ID:'
        print >> headerfile, activerat
        print >> headerfile, 'Passive Rat ID:'
        print >> headerfile, passiverat
        print >> headerfile, 'Number of Trials:'
        print >> headerfile, trialnum
        headerfile.close()


### Start Stages code

        #controls randomness in the stages
        if stagenum == '23' or stagenum == '24':
            TrialId = []
            for i in range(0,int(trialnum)/2):
                TrialId_temp = [1,3] 
                random.shuffle(TrialId_temp)
                TrialId.extend(TrialId_temp)
            print TrialId

        if stagenum == '33' or stagenum == '34':
            TrialId = []
            for i in range(0,int(trialnum)/2):
                TrialId_temp = [1,2,3] 
                random.shuffle(TrialId_temp)
                TrialId.extend(TrialId_temp)
            print TrialId


        if stagenum == '4':
            TrialId = [1,2]
            TrialId = TrialId*(int(trialnum)/2)
            random.shuffle(TrialId)
            print TrialId

        if stagenum == '7':
            TrialId = [1,2,3]
            for i in range(0,int(trialnum)/3):
                TrialId_temp = [1,2,3] 
                random.shuffle(TrialId_temp)
                TrialId.extend(TrialId_temp)
            print TrialId

# Port number notes: Front left = 150, Front right = 15, Back left = 200, Back right = 20.

        nosepokeIDandTime=[0, 0]
        trialstarttimeandID=[0, 0]
        start = datetime.datetime.now()
        #Starts the experiment timer
        experimenttimethread = threading.Thread(None, self.ExperimentTime, None, ())
        experimenttimethread.start()
        trialcount =0
        for x in range(0,trialnum):

## Stage 11
            # stage number 11 is air on self only. Port numbers 200 and 15 turn of airflow.
            # edit only the front right port will turn off air for self (15). Front left will be a dummy port (20). Back ports will be blocked (200 & 150)
            if stagenum == '11':
                #Controls the display for the trial counter
                trialcount=trialcount+1
                trialdisplay = "{0}".format(trialcount)
                self.trialcounter.setDigitCount(len(trialdisplay))
                self.trialcounter.display(trialdisplay)
                StepperControl.SetPosition(1,1.8,1400) #Moves the motors
                imageque.put(1)
                #Starts the trial timer
                trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                trialtimerthread.start()
                move = datetime.datetime.now()
                delta = move - start
                trialstarttimeandID[0] = 1
                trialstarttimeandID[1] = delta.total_seconds()
                print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                Trig = 0
                count = 0
                #Clears the sensor data to ensure that the trial does not end prematurely
                while(not IRsensorque.empty()):
                    CLOSE = IRsensorque.get()
                #Actual trial. Continually searches for signal until recieved.
                while Trig != 15 and Trig != 200 and Trig != 30 and count < 8200: #and Trig != 20 and Trig != 150 and Trig != 200 and Trig != 30:
                    Trig = 0
                    if sensorthread.is_alive():
                        if(not IRsensorque.empty()):
                            Trig = IRsensorque.get()
                            if Trig == 20:
                                nosepokeIDandTime[0]=20
                                press = datetime.datetime.now()
                                delta2 = press - start
                                nosepokeIDandTime[1] = delta2.total_seconds()
                                print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            elif Trig == 150:
                                nosepokeIDandTime[0]=150
                                press = datetime.datetime.now()
                                delta2 = press - start
                                nosepokeIDandTime[1] = delta2.total_seconds()
                                print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    else:
                        sensorthread.start()
                        if(not IRsensorque.empty()):
                            Trig = IRsensorque.get()
                    count += 1
                    time.sleep(.01)
                if Trig == 15:
                    imageque.put(3)
                    nosepokeIDandTime[0]=15
                elif Trig == 200:
                    imageque.put(4)
                    nosepokeIDandTime[0]=200
                elif Trig == 30:
                    #imageque.put(4)
                    nosepokeIDandTime[0]=30
                elif count == 8200:
                    nosepokeIDandTime[0]=40
                IRsensorque.put(0)
                press = datetime.datetime.now()
                if trialtimerthread.is_alive():
                    trialtimeque.put(2)
                else:
                    trialtimerthread.start()
                    trialtimeque.put(2)
                delta1 = press - start
                nosepokeIDandTime[1] = delta1.total_seconds()
                print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                StepperControl.SetPosition(1,1.8,0)
                print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                time.sleep(3)
                imageque.put(0)
                #Interim period
                while(not IRsensorque.empty()):
                    CLOSE = IRsensorque.get()
                if x != trialnum -1:
                    for i in range(0,(delay-3)*10):
                        time.sleep(.1)
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                #if Trig == 150:
                                #    nosepokeIDandTime[0]=-150
                                #    press = datetime.datetime.now()
                                #    delta3 = press - start
                                #    nosepokeIDandTime[1] = delta3.total_seconds()
                                #    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                #elif Trig == 20:
                                #    nosepokeIDandTime[0]=-20
                                #    press = datetime.datetime.now()
                                #    delta3 = press - start
                                #    nosepokeIDandTime[1] = delta3.total_seconds()
                                #    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                if Trig == 200:
                                    nosepokeIDandTime[0]=-200
                                    press = datetime.datetime.now()
                                    delta3 = press - start
                                    nosepokeIDandTime[1] = delta3.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=-15
                                    press = datetime.datetime.now()
                                    delta3 = press - start
                                    nosepokeIDandTime[1] = delta3.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()        
## Stage 12
            # Stage-1 Conditon-2 (coded as stage 12)
            # Airflow on self only. Ports 20 and 150 turn off air.
            # Edited so only port 20 turns off air. Port 15 is a dummy port.
            if stagenum == '12':
                #Controls the display for the trial counter
                trialcount=trialcount+1
                trialdisplay = "{0}".format(trialcount)
                self.trialcounter.setDigitCount(len(trialdisplay))
                self.trialcounter.display(trialdisplay)
                StepperControl.SetPosition(1,1.8,1400) #Moves the motors
                imageque.put(1)
                #Starts the trial timer
                trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                trialtimerthread.start()
                move = datetime.datetime.now()
                delta = move - start
                trialstarttimeandID[0] = 1
                trialstarttimeandID[1] = delta.total_seconds()
                print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                Trig = 0
                count = 0
                #Clears the sensor data to ensure that the trial does not end prematurely
                while(not IRsensorque.empty()):
                    CLOSE = IRsensorque.get()
                #Actual trial. Continually searches for signal until recieved.
                while Trig != 20 and Trig !=150 and Trig != 30 and count < 8200: #Trig != 150 and Trig != 20 and Trig != 150 and Trig != 200 and Trig != 30:
                    Trig = 0
                    if sensorthread.is_alive():
                        if(not IRsensorque.empty()):
                            Trig = IRsensorque.get()
                            if Trig == 200:
                                nosepokeIDandTime[0]=200
                                press = datetime.datetime.now()
                                delta2 = press - start
                                nosepokeIDandTime[1] = delta2.total_seconds()
                                print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            if Trig == 15:
                                nosepokeIDandTime[0]=15
                                press = datetime.datetime.now()
                                delta2 = press - start
                                nosepokeIDandTime[1] = delta2.total_seconds()
                                print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    else:
                        sensorthread.start()
                        if(not IRsensorque.empty()):
                            Trig = IRsensorque.get()
                    count += 1
                    time.sleep(.01)
                if Trig == 150:
                    imageque.put(5)
                    nosepokeIDandTime[0]=150
                if Trig == 20:
                    imageque.put(2)
                    nosepokeIDandTime[0]=20
                elif Trig == 30:
                    imageque.put(4)
                    nosepokeIDandTime[0]=30
                elif count == 8200:
                    nosepokeIDandTime[0]=40
                IRsensorque.put(0)
                press = datetime.datetime.now()
                if trialtimerthread.is_alive():
                    trialtimeque.put(2)
                else:
                    trialtimerthread.start()
                    trialtimeque.put(2)
                delta1 = press - start
                nosepokeIDandTime[1] = delta1.total_seconds()
                print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                StepperControl.SetPosition(1,1.8,0)
                print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                time.sleep(3)
                imageque.put(0)
                #Interim period
                while(not IRsensorque.empty()):
                    CLOSE = IRsensorque.get()
                if x != trialnum -1:
                    for i in range(0,(delay-3)*10):
                        time.sleep(.1)
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                #if Trig == 15:
                                #    nosepokeIDandTime[0]=-15
                                #    press = datetime.datetime.now()
                                #    delta3 = press - start
                                #    nosepokeIDandTime[1] = delta3.total_seconds()
                                #    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                #elif Trig == 200:
                                #    nosepokeIDandTime[0]=-200
                                #    press = datetime.datetime.now()
                                #    delta3 = press - start
                                #    nosepokeIDandTime[1] = delta3.total_seconds()
                                #    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                if Trig == 20:
                                    nosepokeIDandTime[0]=-20
                                    press = datetime.datetime.now()
                                    delta3 = press - start
                                    nosepokeIDandTime[1] = delta3.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 150:
                                    nosepokeIDandTime[0]=-150
                                    press = datetime.datetime.now()
                                    delta3 = press - start
                                    nosepokeIDandTime[1] = delta3.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()


## Stage 21       
            # Stage 21 is air on other (friend) only (Trial ID = 2, motor position -725). Port to turn off air is 20.                
            if stagenum == '21':
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,-725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(6)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 3
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    Trig = 0
                    count = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 20 and Trig != 30 and count < 5900:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 150:
                                    nosepokeIDandTime[0]=150
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=15
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        count += 1
                        time.sleep(.01)
                    if Trig == 20:
                        imageque.put(7)
                        nosepokeIDandTime[0]=20
                    elif Trig == 30:
                        # imageque.put()
                        nosepokeIDandTime[0]=30
                    elif count == 5900:
                        nosepokeIDandTime[0]=40
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Other was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
## Stage 22
            # Air on other (friend only). Port 200 turns off air. 
            if stagenum == '22':
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,-725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(6)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 3
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    Trig = 0
                    count = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 200 and Trig != 30 and count < 5900:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 20:
                                    nosepokeIDandTime[0]=20
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=15
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 150:
                                    nosepokeIDandTime[0]=150
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        count += 1
                        time.sleep(.01)
                    if Trig == 200:
                        imageque.put(9)
                        nosepokeIDandTime[0]=200
                    elif Trig == 30:
                        # imageque.put(4)
                        nosepokeIDandTime[0]=30
                    elif count == 5900:
                        nosepokeIDandTime[0]=40
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
## Stage 23
            # Air alternates between friend/other (trial id = 3) and empty (trial id = 2).
            # Ports 150 turn off for empty and port 20 turns of for friend/other.
            if stagenum == '23':
                TrialId = [2,3,2,3,2,3]
                if TrialId[x] == 2:
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(11) #used to be 5 (Ervey)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 2
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 150 and Trig != 30:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 20:
                                    nosepokeIDandTime[0]=20
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=15
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        time.sleep(.01)
                    if Trig == 150:
                        imageque.put(15) #used to be 7 (Ervey)
                        nosepokeIDandTime[0]=150
                    elif Trig == 30:
                        imageque.put(11) #used to be 4 (Ervey)
                        nosepokeIDandTime[0]=30
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                if TrialId[x] == 3:
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,-725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(6)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 3
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 20 and Trig != 30:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 150:
                                    nosepokeIDandTime[0]=150
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=15
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        time.sleep(.01)
                    if Trig == 20:
                        imageque.put(7)
                        nosepokeIDandTime[0]=20
                    elif Trig == 30:
                        # imageque.put()
                        nosepokeIDandTime[0]=30
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()




## Stage 24
            # Air psuedo-randomly alternates between cagemate and other.
            # Ports 200 turn off for other. Port 15 turns off for empty.
            if stagenum == '24':
                TrialId = [2,3,2,3,2,3]
                if TrialId[x] == 2:
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(11) #used to be 5 (Ervey)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 2
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 15 and Trig != 30:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 20:
                                    nosepokeIDandTime[0]=20
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 150:
                                    nosepokeIDandTime[0]=150
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        time.sleep(.01)
                    if Trig == 15:
                        imageque.put(13) #used to be 7 (Ervey)
                        nosepokeIDandTime[0]=15
                    elif Trig == 30:
                        imageque.put(11) #used to be 4 (Ervey)
                        nosepokeIDandTime[0]=30
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
    
                if TrialId[x] == 3:
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,-725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(6)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 3
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 200 and Trig != 30:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 20:
                                    nosepokeIDandTime[0]=20
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=15
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 150:
                                    nosepokeIDandTime[0]=150
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        time.sleep(.01)
                    if Trig == 200:
                        imageque.put(9)
                        nosepokeIDandTime[0]=200
                    elif Trig == 30:
                        # imageque.put(4)
                        nosepokeIDandTime[0]=30
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
            ## Stage 31
            # Air flows onto empty chamber only.
            # Port 150 turns off airflow on empty.
            if stagenum == '31':
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(11) #used to be 5 (Ervey)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 2
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    count = 0
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 150 and Trig != 30 and count < 5900:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 20:
                                    nosepokeIDandTime[0]=20
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=15
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        count += 1
                        time.sleep(.01)
                    if Trig == 150:
                        imageque.put(15) #used to be 7(Ervey)
                        nosepokeIDandTime[0]=150
                    elif Trig == 30:
                        imageque.put(11) #used to be 4, idk how that's supposed to look like (Ervey)
                        nosepokeIDandTime[0]=30
                    elif count == 5900:
                        nosepokeIDandTime[0]=40
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
## Stage 32
            # Air flows onto empty chamber only.
            # Port 15 turns of air                
            if stagenum == '32':
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(11) #used to be 5 (Ervey)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 2
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    count = 0
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 15 and Trig != 30 and count < 5900:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 20:
                                    nosepokeIDandTime[0]=20
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 150:
                                    nosepokeIDandTime[0]=150
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        count += 1
                        time.sleep(.01)
                    if Trig == 15:
                        imageque.put(13) #used to be 7 (Ervey)
                        nosepokeIDandTime[0]=15
                    elif Trig == 30:
                        imageque.put(11) #used to be 4 (Ervey)
                        nosepokeIDandTime[0]=30
                    elif count == 5900:
                        nosepokeIDandTime[0]=40
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
## Stage 33
            # air psuedo-randomly alternates between self and empty
            # 200 & 15 for self, 150 for empty
            if stagenum == '33':
                if TrialId[x] == 1:
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,1400)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(6)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 1
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    count = 0
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 200 and Trig!= 15 and Trig != 30 and count < 5900:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 20:
                                    nosepokeIDandTime[0]=20
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 150:
                                    nosepokeIDandTime[0]=150
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        count += 1
                        time.sleep(.01)
                    if Trig == 200:
                        imageque.put(14) #used to be 9 (Ervey)
                        nosepokeIDandTime[0]=200
                    elif Trig == 15:
                        imageque.put(13) #used to b4 4 (Ervey)
                        nosepokeIDandTime[0]=15
                    elif Trig == 30:
                        imageque.put(11) #used to be 4 (Ervey)
                        nosepokeIDandTime[0]=30
                    elif count == 5900:
                        nosepokeIDandTime[0]=40
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                if TrialId[x] == 2:
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(11) #used to be 5 (Ervey)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 2
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    count = 0
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 150 and Trig != 30 and count < 3700:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 20:
                                    nosepokeIDandTime[0]=20
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=15
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        count += 1
                        time.sleep(.01)
                    if Trig == 150:
                        imageque.put(15) #used to be 7 (Ervey)
                        nosepokeIDandTime[0]=150
                    elif Trig == 30:
                        imageque.put(11) #used to be 4 (Ervey)
                        nosepokeIDandTime[0]=30
                    elif count == 3700:
                        nosepokeIDandTime[0]=40
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                if TrialId[x] == 3:
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,-725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(6)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 3
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    count = 0
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 20 and Trig != 30 and count < 5900:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 150:
                                    nosepokeIDandTime[0]=150
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=15
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        count += 1
                        time.sleep(.01)
                    if Trig == 20:
                        imageque.put(7)
                        nosepokeIDandTime[0]=20
                    elif Trig == 30:
                        # imageque.put()
                        nosepokeIDandTime[0]=30
                    elif count == 5900:
                        nosepokeIDandTime[0]=40
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
              
## Stage 34
            # air psudo-randomly alternates between self and empty. 
            # 150 & 20 = self, 15 = empty                
            if stagenum == '34':
                if TrialId[x] == 1:
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,1400)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(11) #used to be 6 (Ervey)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 1
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    count = 0
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 150 and Trig != 20 and Trig != 30 and count < 3700:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 15:
                                    nosepokeIDandTime[0]=15
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        count += 1
                        time.sleep(.01)
                    if Trig == 150:
                        imageque.put(15) #used to be 9 (Ervey)
                        nosepokeIDandTime[0]=20
                    elif Trig == 20:
                        imageque.put(12) #used to be 4 (Ervey)
                        nosepokeIDandTime[0]=150
                    elif Trig == 30:
                        imageque.put(11) #used to be 4 (Ervey)
                        nosepokeIDandTime[0]=30
                    elif count == 3700:
                        nosepokeIDandTime[0]=40
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                if TrialId[x] == 2:
                    trialcount=trialcount+1
                    trialdisplay = "{0}".format(trialcount)
                    self.trialcounter.setDigitCount(len(trialdisplay))
                    self.trialcounter.display(trialdisplay)
                    StepperControl.SetPosition(1,1.8,725)
                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
                    trialtimerthread.start()
                    imageque.put(11) #used to be 5 (Ervey)
                    move = datetime.datetime.now()
                    delta = move - start
                    trialstarttimeandID[0] = 2
                    trialstarttimeandID[1] = delta.total_seconds()
                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
                    count = 0
                    Trig = 0
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    while Trig != 15 and Trig != 30 and count < 3700:
                        Trig = 0
                        if sensorthread.is_alive():
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                                if Trig == 20:
                                    nosepokeIDandTime[0]=20
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 150:
                                    nosepokeIDandTime[0]=150
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                elif Trig == 200:
                                    nosepokeIDandTime[0]=200
                                    press = datetime.datetime.now()
                                    delta2 = press - start
                                    nosepokeIDandTime[1] = delta2.total_seconds()
                                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                        else:
                            sensorthread.start()
                            if(not IRsensorque.empty()):
                                Trig = IRsensorque.get()
                        count += 1
                        time.sleep(.01)
                    if Trig == 15:
                        imageque.put(13) #used to be 7 (Ervey)
                        nosepokeIDandTime[0]=15
                    elif Trig == 30:
                        imageque.put(11) #used to be 4 (Ervey)
                        nosepokeIDandTime[0]=30
                    elif count == 3700:
                        nosepokeIDandTime[0]=40
                    press = datetime.datetime.now()
                    if trialtimerthread.is_alive():
                        trialtimeque.put(2)
                    else:
                        trialtimerthread.start()
                        trialtimeque.put(2)
                    delta1 = press - start
                    nosepokeIDandTime[1] = delta1.total_seconds()
                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
                    StepperControl.SetPosition(1,1.8,0)
                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                    time.sleep(3)
                    imageque.put(0)
                    while(not IRsensorque.empty()):
                        CLOSE = IRsensorque.get()
                    if x != trialnum -1:
                        for i in range(0,(delay-3)*10):
                            time.sleep(.1)
                            Trig = 0
                            if sensorthread.is_alive():
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                                    if Trig == 150:
                                        nosepokeIDandTime[0]=-150
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 200:
                                        nosepokeIDandTime[0]=-200
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 20:
                                        nosepokeIDandTime[0]=-20
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                                    elif Trig == 15:
                                        nosepokeIDandTime[0]=-15
                                        press = datetime.datetime.now()
                                        delta3 = press - start
                                        nosepokeIDandTime[1] = delta3.total_seconds()
                                        print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
                            else:
                                sensorthread.start()
                                if(not IRsensorque.empty()):
                                    Trig = IRsensorque.get()
                    
                
#### Stage numbers: 3, 4, 5, 6, 7. Not currently being used.                            
##            if stagenum == '3':
##                if TrialId[x] == 1:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,-1450)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(6)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = 1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 20 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 15:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 3
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    if Trig == 20:
##                        imageque.put(9)
##                        nosepokeIDandTime[0]=2
##                    elif Trig == 30:
##                        imageque.put(4)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                if TrialId[x] == 2:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,725)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(5)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = -1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 15 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 20:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 2
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    nosepokeIDandTime[0]=1
##                    if Trig == 15:
##                        imageque.put(7)
##                        nosepokeIDandTime[0]=3
##                    elif Trig == 30:
##                        imageque.put(4)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##
##            if stagenum == '4':
##                if TrialId[x] == 1:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,-1450)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(6)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = 1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 20 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 15:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 3
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    if Trig == 20:
##                        imageque.put(9)
##                        nosepokeIDandTime[0]=2
##                    elif Trig == 30:
##                        imageque.put(4)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                if TrialId[x] == 2:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,725)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(5)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = -1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 15 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 20:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 2
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    nosepokeIDandTime[0]=1
##                    if Trig == 15:
##                        imageque.put(7)
##                        nosepokeIDandTime[0]=3
##                    elif Trig == 30:
##                        imageque.put(4)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##
##            if stagenum == '5':
##                if TrialId[x] == 1:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,-1450)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(6)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = 1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 20 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 15:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 3
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    if Trig == 20:
##                        imageque.put(9)
##                        nosepokeIDandTime[0]=2
##                    elif Trig == 30:
##                        imageque.put(4)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                if TrialId[x] == 2:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,-725)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(10)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = -1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 15 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 20:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 2
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    nosepokeIDandTime[0]=1
##                    if Trig == 15:
##                        imageque.put(11)
##                        nosepokeIDandTime[0]=3
##                    elif Trig == 30:
##                        imageque.put(12)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##
##
##        #stage 6 between empty and friend. Random, but can't have more than 3 same trials in a row
##            if stagenum == '6':
##                if TrialId[x] == 1:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8, 725)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(6)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = 1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 20 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 15:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 3
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    if Trig == 20:
##                        imageque.put(9)
##                        nosepokeIDandTime[0]=2
##                    elif Trig == 30:
##                        imageque.put(4)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##
##                    
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                if TrialId[x] == 2:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,-725)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(10)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = -1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 15 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 20:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 2
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    nosepokeIDandTime[0]=1
##                    if Trig == 15:
##                        imageque.put(11)
##                        nosepokeIDandTime[0]=3
##                    elif Trig == 30:
##                        imageque.put(12)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##
##                    StepperControl.SetPosition(1,1.8,0)
##                
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##
##
##          #stage 7 all three chambers
##            if stagenum == '7':
##                 if TrialId[x] == 1:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,-1450)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(6)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = 1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 20 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 15:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 3
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    if Trig == 20:
##                        imageque.put(9)
##                        nosepokeIDandTime[0]=2
##                    elif Trig == 30:
##                        imageque.put(4)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                 if TrialId[x] == 2:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,725)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(10)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = -1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 15 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 20:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 2
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    nosepokeIDandTime[0]=1
##                    if Trig == 15:
##                        imageque.put(11)
##                        nosepokeIDandTime[0]=3
##                    elif Trig == 30:
##                        imageque.put(12)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            
##                 if TrialId[x] == 3:
##                    trialcount=trialcount+1
##                    trialdisplay = "{0}".format(trialcount)
##                    self.trialcounter.setDigitCount(len(trialdisplay))
##                    self.trialcounter.display(trialdisplay)
##                    StepperControl.SetPosition(1,1.8,-725)
##                    trialtimerthread = threading.Thread(None, self.Trialtime, None, ())
##                    trialtimerthread.start()
##                    imageque.put(10)
##                    move = datetime.datetime.now()
##                    delta = move - start
##                    trialstarttimeandID[0] = -1
##                    trialstarttimeandID[1] = delta.total_seconds()
##                    print >> datafile, str(trialstarttimeandID[0]), str(trialstarttimeandID[1]).rjust(savefilespacing)
##                    Trig = 0
##                    while(not IRsensorque.empty()):
##                        CLOSE = IRsensorque.get()
##                    while Trig != 15 and Trig != 30:
##                        Trig = 0
##                        if sensorthread.is_alive():
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        else:
##                            sensorthread.start()
##                            if(not IRsensorque.empty()):
##                                Trig = IRsensorque.get()
##                        time.sleep(.01)
##                        if Trig == 20:
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[0] = 2
##                            nosepokeIDandTime[1] = delta1.total_seconds()
##                            print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    nosepokeIDandTime[0]=1
##                    if Trig == 15:
##                        imageque.put(11)
##                        nosepokeIDandTime[0]=3
##                    elif Trig == 30:
##                        imageque.put(12)
##                        nosepokeIDandTime[0]=4
##                    press = datetime.datetime.now()
##                    if trialtimerthread.is_alive():
##                        trialtimeque.put(2)
##                    else:
##                        trialtimerthread.start()
##                        trialtimeque.put(2)
##                    delta1 = press - start
##                    nosepokeIDandTime[1] = delta1.total_seconds()
##                    print "Rat_Lever_Self was triggered at", nosepokeIDandTime[1]
##                    StepperControl.SetPosition(1,1.8,0)
##                    print >> datafile, str(nosepokeIDandTime[0]), str(nosepokeIDandTime[1]).rjust(savefilespacing)
##                    time.sleep(3)
##                    imageque.put(0)
##                    if x != trialnum -1:
##                        for i in range(0,(delay-3)*10):
##                            time.sleep(.1)
##                            Trig = 0
##                            if sensorthread.is_alive():
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            else:
##                                sensorthread.start()
##                                if(not IRsensorque.empty()):
##                                    Trig = IRsensorque.get()
##                            if Trig == 15:
##                                nosepokeIDandTime[0]=3
##                            elif Trig == 20:
##                                nosepokeIDandTime[0]=2
##                            elif Trig == 30:
##                                nosepokeIDandTime[0]=4
##                            press = datetime.datetime.now()
##                            delta1 = press - start
##                            nosepokeIDandTime[1] = delta1.total_seconds()      
##
### End of stages code     
                      
          
                   

        datafile.close()
        experimenttimeque.put(1)
        experimentendque.put(1)
        if sensorthread.is_alive():
            IRsensorque.put(25)
        else:
            print "File save thread died"
        print "Trials concluded, file successfully saved."
        timerthread.put(1)
        time.sleep(1)
        cv2.destroyAllWindows()
        cameraoutput.release()
        camera.release()
        time.sleep(1)


class Canvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class matplotlibWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = Canvas()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

if __name__ == "__main__":
    import sys
    global cameraoutput, camera
    app = QtGui.QApplication(sys.argv)
    EmpathyTrialGUI = QtGui.QMainWindow()
    ui = Ui_EmpathyTrialGUI()
    ui.setupUi(EmpathyTrialGUI)
    EmpathyTrialGUI.show()

    #Starts all of the queues for the experiment. Necessary for multithreading
    imageque = Queue.Queue()
    trialtimeque = Queue.Queue()
    experimenttimeque = Queue.Queue()
    IRsensorque = Queue.Queue()
    experimentcountque = Queue.Queue()
    trialcountque = Queue.Queue()
    experimentendque = Queue.Queue()
    timerthread = Queue.Queue()
    #Connects Arduino to Python
    COMId = 6
    StepperControl =InstrumentControl.StepperMotor('COM%d' %COMId)
    def appExec():
        app.exec_()
        
    sys.exit(appExec())
